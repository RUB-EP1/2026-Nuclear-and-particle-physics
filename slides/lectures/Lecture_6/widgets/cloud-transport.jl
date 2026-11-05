# Run with the saved 2025 G4Examples.jl environment; no package updates required.
using Geant4
using Geant4.SystemOfUnits
using Random
Random.seed!(20261030)

struct AirChamber <: G4JLDetector end
function construct(::AirChamber)::CxxPtr{G4VPhysicalVolume}
    air = FindOrBuildMaterial(G4NistManager!Instance(), "G4_AIR")
    solid = G4Box("air", 100mm, 100mm, 25mm)
    logical = G4LogicalVolume(solid, air, "Air")
    G4PVPlacement(nothing, G4ThreeVector(), logical, "Air", nothing, false, 0, true)
end
Geant4.getConstructor(::AirChamber)::Function = construct

const segments = Any[]
function record(step::G4Step, ::G4JLApplication)::Nothing
    edep = GetTotalEnergyDeposit(step) / keV
    edep <= 0 && return nothing
    track = GetTrack(step)
    name = String(GetParticleName(GetParticleDefinition(track)))
    name in ("gamma", "neutron", "nu_mu", "anti_nu_mu") && return nothing
    a = GetPosition(GetPreStepPoint(step))
    b = GetPosition(GetPostStepPoint(step))
    # Julia's G4ThreeVector supports x/y/z accessors.
    push!(segments, [name, Int(GetTrackID(track)),
                    round.([x(a)/mm,y(a)/mm,z(a)/mm,x(b)/mm,y(b)/mm,z(b)/mm,edep]; digits=4)...])
    nothing
end

gun = G4JLGunGenerator(particle="mu-", energy=4GeV, direction=G4ThreeVector(0,0,-1))
app = G4JLApplication(detector=AirChamber(), generator=gun, physics_type=FTFP_BERT,
                     stepaction_method=record, nthreads=0)
configure(app)
initialize(app)
ui = G4UImanager!GetUIpointer()
ApplyCommand(ui, "/run/setCut 0.1 mm")
beamOn(app, 0)
events = String[]
for kind in ("muon", "alpha", "electron")
    for i in 1:50
        empty!(segments)
        if kind == "muon"
            # I(theta) proportional to cos^2(theta); horizontal-plane arrivals
            # add projected area cos(theta): cos(theta) = U^(1/4).
            c = rand()^0.25; phi=2pi*rand(); s=sqrt(1-c*c)
            dir = G4ThreeVector(s*cos(phi),s*sin(phi),-c)
            pos = G4ThreeVector(198rand()-99,198rand()-99,24.99)
            particle = rand()<0.56 ? "mu+" : "mu-"
            energy = 4GeV # representative energy, not a cosmic energy spectrum
        else
            c=2rand()-1; phi=2pi*rand(); s=sqrt(1-c*c)
            dir=G4ThreeVector(s*cos(phi),s*sin(phi),c)
            pos=G4ThreeVector(198rand()-99,198rand()-99,48rand()-24)
            particle=kind=="alpha" ? "alpha" : "e-"
            # Rn-222 alpha; representative background electron energy bank.
            energy=kind=="alpha" ? 5.49MeV : (0.05+0.95rand())*MeV
        end
        SetParticleByName(gun,particle)
        SetParticleEnergy(gun,energy)
        SetParticlePosition(gun,pos)
        SetParticleMomentumDirection(gun,dir)
        beamOn(app,1)
        # JSON without adding dependencies. All values are finite scalars/strings.
        rows = ["[\"$(r[1])\"," * join(r[2:end],",") * "]" for r in segments]
        push!(events,"{\"kind\":\"$kind\",\"energyMeV\":$(energy/MeV),\"segments\":["*join(rows,",")*"]}")
    end
end
open(joinpath(@__DIR__,"cloud-events.json"),"w") do io
    write(io,"["*join(events,",")*"]")
end
println("WROTE ",length(events)," GEANT4 EVENTS")

# Lecture 6 quiz: Interactions with matter

Implemented in Mentimeter: [Edit](https://www.mentimeter.com/app/presentation/al8jv63eexfyiaybx3iinwohyfwqcrwk/edit) · [Present](https://www.mentimeter.com/app/presentation/al8jv63eexfyiaybx3iinwohyfwqcrwk/present).

Six multiple-choice questions, with one
correct answer per question. Preserve the question order and answer choices.
Keep the answer explanations for the presenter, separate from participant prompts.

Scope: luminosity and selected event yields, plus original Lecture 5 slides 19–37,
excluding Energy-loss fluctuations.
Run after the review of critical energy and before **3 · Multiple scattering**.

## Question 1 · From luminosity to reconstructed decays

Consider an LHCb-like sample of proton–proton collisions at √s = 7 TeV.
Use these rounded values:

- Integrated luminosity: Lᵢₙₜ = 1 fb⁻¹.
- **B⁺ production cross section** in the LHCb fiducial region: σ(B⁺) = 20 μb.
- Branching fraction: BR(B⁺ → π⁺π⁻π⁺) = 1.5 × 10⁻⁵.
- Overall reconstruction and selection efficiency for these decays: ε = 10%.

How many **reconstructed B⁺ → π⁺π⁻π⁺ decays** do you expect?
Count B⁺ only, not B⁻. Use 1 μb = 10⁹ fb.

**A.** 3 × 10³.

**B.** 3 × 10⁵.

**C.** 3 × 10⁴.

**D.** 2 × 10⁹.

**Correct: C — about 30,000 reconstructed decays.**

**N = Lᵢₙₜ × σ(B⁺) × BR × ε**

N = 1 × (20 × 10⁹) × (1.5 × 10⁻⁵) × 0.10 = **30,000**.

Presenter explanation: first produce 2 × 10¹⁰ B⁺ mesons in the
fiducial region; about 3 × 10⁵ decay into the specified three-pion final
state; select 10% of those. B omits efficiency; D omits the branching fraction.
The efficiency is an assumed, decay-averaged exercise input, not a quoted LHCb
measurement. It applies to decays of B⁺ mesons already in the quoted fiducial
region, so do not multiply by another parent-acceptance factor.

**Input provenance (for the presenter):**

- [LHCb, JHEP 04 (2012) 093](https://arxiv.org/abs/1202.4812)
  measured σ(B⁺ + B⁻) = 41.4 μb at 7 TeV for
  0 < pₜ < 40 GeV/c and 2.0 < y < 4.5. Assuming equal production of
  the two charges gives 20.7 μb for B⁺ alone, rounded here
  to 20 μb. Do not use the charge-summed cross section for a
  positive-charge-only yield.
- [BaBar, Phys. Rev. D 79 (2009) 072006](https://doi.org/10.1103/PhysRevD.79.072006)
  measured the charge-averaged three-charged-pion branching fraction as
  (15.2 ± 0.6 ± 1.2 ± 0.4) × 10⁻⁶. Use 15 × 10⁻⁶ for this
  estimate, neglecting charge asymmetry.

## Question 2 · Thickness and ionization

A minimum-ionizing particle crosses a thin silicon sensor.
An identical particle crosses **twice the silicon thickness**.
Assume neither particle slows appreciably. How does the **mean energy loss** change?

**A.** It stays the same because both particles are minimum-ionizing.

**B.** It doubles.

**C.** It increases by a factor of four.

**D.** It halves.

**Correct: B.** ⟨ΔE⟩ ≈ Sₘ ρ ℓ: unchanged stopping power and density, twice the path length. Minimum-ionizing describes a minimum of energy loss per unit mass thickness, not a fixed total energy deposit.

## Question 3 · Mass and particle identification

A proton and a charged pion have the **same momentum** and |z| = 1.
Both are on the low-velocity, approximately 1/β² part of the ionization curve.
Which has the larger mean ionization loss per unit length?

**A.** The pion, because it is lighter.

**B.** They have the same loss because their momenta are equal.

**C.** They have the same loss because their charge magnitudes are equal.

**D.** The proton, because it is slower.

**Correct: D.** At fixed momentum, βγ = p/(Mc) is smaller for the heavier proton, and so is its speed. In the stated regime the 1/β² dependence gives larger ionization loss. This ordering is not universal across the entire Bethe–Bloch curve. Momentum and ionization together allow mass discrimination.

## Question 4 · Where is the TPC hit?

Two electron clouds are created at the same time in a TPC and drift to the same readout plane.
Cloud B arrives **later** than cloud A. The drift speed is uniform.
What does this tell us?

**A.** B was created farther from the readout plane along the drift direction.

**B.** B was created by a particle with larger momentum.

**C.** B contains more ionization electrons.

**D.** B was created closer to the readout plane.

**Correct: A.** The drift distance is d = v_d (t − t₀). Pads supply the two coordinates in the readout plane; arrival time supplies the drift coordinate when the creation time is known. Momentum is inferred from track curvature in the magnetic field, not from electron arrival time.

## Question 5 · Bethe–Bloch: what is a MIP?

A pion and a proton, both with charge +e, cross the same material.
Each is near the **minimum of its Bethe–Bloch curve**, at βγ ≈ 3–4.
Which statement is approximately correct?

**A.** They have the same momentum and the same mean ionization loss per unit length.

**B.** The proton has a larger momentum, but their mean ionization losses per unit length are similar.

**C.** The proton loses much more energy per unit length because it is heavier.

**D.** Both lose essentially no energy: minimum-ionizing means no ionization.

**Correct: B.** The Bethe–Bloch curve depends primarily on charge and speed,
not directly on particle mass. Near the minimum, particles with the same charge
in the same material have similar mean ionization losses per unit length.
However, p = Mc βγ, so the heavier proton needs a larger momentum
to reach the same βγ (about 6.7 times the pion momentum).
“MIP” describes a velocity regime, not a particle species, and the minimum
stopping power is nonzero.

## Question 6 · What does critical energy mean?

An electron has energy equal to the **critical energy** E_c of a material.
Which statement describes this crossover?

**A.** The electron first becomes able to ionize atoms.

**B.** Mean radiative and collisional energy losses per unit length are approximately equal.

**C.** The electron must lose all its energy in one collision.

**D.** Bremsstrahlung is forbidden below this energy.

**Correct: B.** S_rad(E_c) ≈ S_coll(E_c). Below the crossover, collision losses dominate; above it, radiation dominates. Dominance is not a threshold: both mechanisms can operate on either side. Different conventions for critical energy give slightly different numerical values.

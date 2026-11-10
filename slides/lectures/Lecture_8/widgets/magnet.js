'use strict';
// Parts of the LHC main dipole cryomagnet. Facts are rounded values from the LHC Design Report and CERN public material.
const PARTS = {
  beam: { name: 'Proton beams', temp: 'Two beams, opposite directions', what: 'Two counter-rotating beams pass through the same magnet, 194 mm apart. The field points up in one aperture and down in the other, so both beams bend the same way round the ring.', fact: 'A bunch is only millimetres wide here; at the collision points it is squeezed to about 17 µm.' },
  screen: { name: 'Beam screen', temp: '5–20 K', what: 'A perforated, copper-lined steel tube inside the cold bore. It intercepts synchrotron light and heat from image currents before they reach the 1.9 K magnet.', fact: 'The LHC protons radiate only a few kW per beam — but every watt at 1.9 K costs roughly a kilowatt of electrical power at room temperature to remove.' },
  coldbore: { name: 'Cold bore (beam pipe)', temp: '1.9 K', what: 'The vacuum chamber, 50 mm in inner diameter, in contact with the superfluid helium. Its cold walls act as a pump: gas molecules freeze onto them.', fact: 'The beam vacuum is about 10⁻¹³ atmospheres — emptier than the atmosphere on the Moon.' },
  coil: { name: 'Superconducting coils', temp: '1.9 K', what: 'Two layers of niobium–titanium cable wound around each aperture. The current distribution (roughly ∝ cos θ) produces a uniform vertical field of 8.33 T at 11 850 A.', fact: 'The LHC contains about 7 600 km of this cable; its fine Nb–Ti filaments would reach the Sun and back several times.' },
  collar: { name: 'Collars', temp: '1.9 K', what: 'Stainless-steel laminations clamped around both coils. They hold the windings in place against the magnetic forces, which try to push the coils outwards.', fact: 'At full field the forces on the coils reach hundreds of tonnes per metre of magnet; a movement of a few micrometres can release enough heat to quench.' },
  yoke: { name: 'Iron yoke', temp: '1.9 K', what: 'Low-carbon steel around the collared coils. It returns the magnetic flux, strengthens the field in the apertures and keeps the field from leaking outside.', fact: 'Coils, collars, yoke and shell form the "cold mass": about 27 tonnes per 15 m dipole, all cooled to 1.9 K.' },
  shell: { name: 'Helium vessel (shrinking cylinder)', temp: '1.9 K, ~1 bar', what: 'Two steel half-shells welded around the yoke. The space inside is filled with superfluid helium, which flows through tiny gaps and carries heat away.', fact: 'Superfluid helium (below 2.17 K) conducts heat far better than copper. The LHC holds roughly a hundred tonnes of helium.' },
  hx: { name: 'Heat-exchanger pipe', temp: '1.8 K, ~16 mbar', what: 'A tube along the top of the magnet carrying helium boiling at low pressure. It cools the pressurised superfluid bath around the magnet by a small temperature difference.', fact: 'One pipe runs continuously through each 107 m cooling loop; the whole ring is cooled in sectors of 3.3 km.' },
  busbar: { name: 'Bus bars', temp: '1.9 K', what: 'Superconducting cables that carry the 11.85 kA current from one magnet to the next. All dipoles of a sector are powered in series.', fact: 'On 19 September 2008 a faulty soldered joint between two bus bars failed, causing an electrical arc and serious damage; the LHC restarted in November 2009 with improved protection.' },
  shield: { name: 'Thermal shield', temp: '~50–75 K', what: 'An aluminium screen wrapped in multilayer insulation. It intercepts heat radiated from the room-temperature vessel before it reaches the cold mass.', fact: 'Thermal radiation scales as T⁴: a shield at 60 K reduces the radiated heat on the cold mass by orders of magnitude.' },
  vacuum: { name: 'Insulation vacuum', temp: 'between 300 K and 1.9 K', what: 'The space between the vacuum vessel and the cold mass is pumped out so that gas cannot conduct heat inwards — like a giant thermos flask.', fact: 'This is a separate vacuum from the beam vacuum: the beam pipe is sealed inside the cold mass.' },
  vessel: { name: 'Vacuum vessel', temp: 'Room temperature', what: 'The blue steel tube you see in the tunnel photo, 914 mm in diameter. It carries the whole assembly and seals the insulation vacuum.', fact: 'There are 1 232 of these dipoles, each about 15 m long, filling about 2/3 of the 26.7 km ring.' },
  post: { name: 'Support posts', temp: '300 K → 1.9 K', what: 'Glass-fibre epoxy columns that hold the 27-tonne cold mass inside the vessel while letting very little heat flow through them.', fact: 'Three posts per dipole: strong enough to carry the cold mass, while the heat leaking through them is only a fraction of a watt at 1.9 K.' }
};
const ORDER = ['beam', 'screen', 'coldbore', 'coil', 'collar', 'yoke', 'shell', 'hx', 'busbar', 'shield', 'vacuum', 'vessel', 'post'];
const $ = id => document.getElementById(id);
function select(k) {
  const p = PARTS[k];
  $('name').textContent = p.name; $('temp').textContent = p.temp; $('what').textContent = p.what; $('fact').textContent = p.fact;
  document.querySelectorAll('.part').forEach(el => el.classList.toggle('sel', el.dataset.k === k));
  document.querySelectorAll('#list button').forEach(b => b.classList.toggle('on', b.dataset.k === k));
  window.magnetState = { selected: k };
}
for (const k of ORDER) { const b = document.createElement('button'); b.textContent = PARTS[k].name.replace(/ \(.*\)/, ''); b.dataset.k = k; b.onclick = () => select(k); $('list').appendChild(b); }
document.querySelectorAll('.part').forEach(el => el.addEventListener('click', e => { e.stopPropagation(); select(el.dataset.k); }));
select('coil');

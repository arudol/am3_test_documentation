# List of switches
The flexibility of AM3 is implemented by *switches* which allow to turn on/off processes in much detail. Below we give a full list of all switches available, which are attributes of a `SimulationManager` instance `sim`. 
Note that some are *multiplicative switches* that may be used to turn off all aspects of a certain process.

## Physics Processes

### Synchrotron
- Electrons: Use `sim.process_esy` to turn on/off all electron synchrotron related processes. In detail, `sim.process_esyrad` controls whether electron synchrotron produces photons, `sim.process_esycool` whether electrons cool due to synchrotron and `sim.process_qsyn` is the switch for quantum synchrotron emission.
- Photons: `sim.process_ssa`
- Protons: Use `sim.process_psy` to turn on/off all proton synchrotron related processes. In detail, `sim.process_psyrad` controls whether proton synchrotron produces photons and  `sim.process_psycool` whether protons cool due to synchrotron emission.
- Muons: Use `sim.process_musy` to turn on/off all muon synchrotron related processes. In detail, `sim.process_musyrad` controls whether muons synchrotron produces photons and `sim.process_musycool` whether muons cool due to synchrotron emission.
- Pions: Use `sim.process_pisy` to turn on/off all muon synchrotron related processes. In detail,  `sim.process_pisyrad` controls whether muons synchrotron produces photons and `sim.process_pisycool` whether pions cool due to synchrotron emission.

In addition, `sim.SetHadronicSy` can be used to turn `sim.process_psy` = `sim.process_musy` = `sim.process_pisy` on or off.

### Inverse Compton

- Electrons: `sim.process_eic` `sim.process_eicrad` `sim.process_eicrad_fast` `sim.eicrad_fast_n_photon_in` `sim.eicrad_fast_n_photon_out` `sim.eicrad_fast_photon_in_max` `sim.eicrad_fast_photon_out_min` `sim.process_eiccool` `sim.process_eic_photonLoss`
- Protons: `sim.process_pic` `sim.process_picrad` `sim.process_piccool`
- Muons: `sim.process_muic` `sim.process_muicrad` `sim.process_muiccool`
- Pions: `sim.process_piic` `sim.process_piicrad` `sim.process_piiccool`

`sim.SetHadronicIC`

### Photo-pion production
- `sim.process_pg`
- `sim.process_pgrad`
- `sim.process_pgrad_fast`
- `sim.pgrad_fast_n_photon_in`
- `sim.pgrad_fast_photon_in_max`
- `sim.process_pgcool`
- `sim.process_pg_photonLoss`

### Bethe-Heitler (photo-pair production)
- `sim.process_bh`
- `sim.process_bhrad`
- `sim.process_bhrad_fast`
- `sim.bhrad_fast_n_el_out`
- `sim.bhrad_fast_proton_in_min`
- `sim.bhrad_fast_photon_in_max`
- `sim.process_bhcool`

### Proton-Proton interaction


### $\gamma \gamma$-annihilation
- `sim.process_pair`
- `sim.process_pair_photonLoss`
- `sim.process_pair_feedback`
- `sim.process_pair_feedback_8bin`

### Secondary decay
- `sim.process_sec_decay`
- `sim.process_pi_decay`
- `sim.process_mu_decay`

### Expansion
- `sim.process_adi`
- `sim.process_exp`

### Injection and Escape
Escape:
- `sim.process_es`
- `sim.escape_type`
Injection:
- `sim.process_in`
- `sim.internal_inj_type`
- `sim.process_inext`

## Solver

- `sim.solver_threshold_cool_dom`
- `sim.solver_threshold_esc_dom`
- `sim.solver_threshold_matrix`
- `sim.solver_simpleqintegration`


## Miscallaneous

- `sim.process_parse_sed`
- `sim.process_hadronic`
- `sim.process_mergePositronsIntoElectrons`
- `sim.verbose`
- `sim.profile_timing`  . `sim.get_timing()`
- `sim.SetLepOptimizer` and `sim.SetHadOptimizer`
- `sim.estimate_max_energies`
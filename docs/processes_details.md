# Physics processes details: List of switches

The flexibility of AM3 is implemented by *switches* which allow to turn on/off processes in much detail. Below we give a full list of all switches available, which are attributes of a `SimulationManager` instance `sim`. 
Note that some are *multiplicative switches* that may be used to turn off all aspects of a certain process.

## Physics Processes

### Synchrotron
- Electrons: `sim.process_esy`, `sim.process_esyrad`, `sim.process_esycool`, `sim.process_qsyn`
- Photons: `sim.process_ssa`
- Protons:`sim.process_psy` , `sim.process_psyrad`, `sim.process_psycool`
- Muons: `sim.process_musy` , `sim.process_musyrad`, `sim.process_musycool`
- Pions:`sim.process_pisy` , `sim.process_pisyrad`, `sim.process_pisycool`

`sim.SetHadronicSy`

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
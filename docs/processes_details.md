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

- Electrons: `sim.process_eic` `sim.process_eicrad` `sim.process_eiccool` `sim.process_eic_photonLoss`
- Optimization of the electron inverse Compton. `sim.process_eicrad_fast` `sim.eicrad_fast_n_photon_in` `sim.eicrad_fast_n_photon_out` `sim.eicrad_fast_photon_in_max` `sim.eicrad_fast_photon_out_min` 
- Protons: Use `sim.process_pic` to turn on/off all proton inverse Compton related processes. In detail, `sim.process_picrad` controls whether proton inverse Compton produces photons and `sim.process_piccool` whether protons cool due to inverse Compton scatterings.
- Muons: Use `sim.process_muic` to turn on/off all muon inverse Compton related processes. In detail, `sim.process_muicrad` controls whether muon inverse Compton produces photons and `sim.process_muiccool` whether muons cool due to inverse Compton scatterings.
- Pions: Use `sim.process_piic` to turn on/off all pion inverse Compton related processes. In detail, `sim.process_piicrad` controls whether pion inverse Compton produces photons and `sim.process_piiccool` whether pions cool due to inverse Compton scatterings.

In addition, `sim.SetHadronicIC` can be used to turn `sim.process_pic` = `sim.process_muic` = `sim.process_piic` on or off.

### Photo-pion production
- The overall multiplicative switch is `sim.process_pg`, used to turn the process on/off.
- `sim.process_pgrad`
- `sim.process_pgrad_fast`  `sim.pgrad_fast_n_photon_in`  `sim.pgrad_fast_photon_in_max`
- `sim.process_pgcool`
- `sim.process_pg_photonLoss`

### Bethe-Heitler (photo-pair production)
- The overall multiplicative switch is `sim.process_bh`, used to turn the process on/off.
- `sim.process_bhrad` 
- `sim.process_bhrad_fast` `sim.bhrad_fast_n_el_out` `sim.bhrad_fast_proton_in_min` `sim.bhrad_fast_photon_in_max`
- `sim.process_bhcool`

### Proton-Proton interaction


### $\gamma \gamma$-annihilation
- The overall multiplicative switch is `sim.process_pair`, used to turn the process on/off.
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

- `sim.process_parse_sed` is used to switch on the tracking of leptons and photons by process they originate from.
- `sim.process_hadronic` is a multiplicative switch that can switch off all hadronic processes.
- `sim.process_mergePositronsIntoElectrons` merges positrons and electrons in a single population. As electron-positrion annihilation is not included, this does not yield different results for synchrotron and inverse Compton emission of these populations.
- `sim.verbose`
- `sim.profile_timing`  . `sim.get_timing()`
- `sim.SetLepOptimizer` and `sim.SetHadOptimizer`
- `sim.estimate_max_energies`
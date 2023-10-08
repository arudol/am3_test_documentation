# Code details

To evolve number densities $n$ as a function of time $t$ AM3 solves the time-dependent partial differential equations of the form

$$ \partial_{t}n(E,t)=-\partial_{E} \dot{E}({E,t})n(E,t)-\alpha(E,t) n(E,t)+Q(E,t) $$

It thus accounts for cooling [ $\dot{E}(E,t)$ ], escape/sink [ $\alpha(E,t)$ ] and injection/source [ $Q(E,t)$  ].


## Code structure

The user-interface module contains five classes:

  * 'SimulationManager' is the core class managing a simulation. Objects of this class will be referred to as 'sim'.
  * 'PhysicsHandler' is a helper class to collect all physics processes. It does not have to be accessed, only initialisation is required. Objects of this class will be referred to as 'ph'.
  * 'RunParams' holds the simulation parameters, such as the source details. Objects of this class will be referred to as 'rp'.
  * 'AM3Arrays' holds the data arrays during the simulation. It does not have to be accessed, only initialisation is required. Objects of this class will be referred to as 'dat'.
  * 'IO' contains the input/output possibilities. Objects of this class will be referred to as 'io'.

Note that internally all physics processes are implemented in single modules (i.e. .cc files), which however is only relevant on developer level.

## Grids

Code-internal we differentiate between three energy grids: The lepton ($e^\pm$), photon ($\gamma$) and hadronic (all other particles) ones; all equally spaced in logarithmic space (base e). The grid settings are specified during compilation and thus cannot be changed during runtime. 
Grid parameters and access:
* *Definition of energy grids* is done in include/AM3/global_defs.h .
    Photon grid length is defined by BIN_X, photon grid origin X_I. The other grid lengths are derived: BIN_E = BIN_X + X_I, BIN_P = BIN_E - 26. Grid spacing D_X = 0.1 (in e base) is not be changed, as this would lead to erroneous results.
* *Readout of grids* is via object io of class IO:
    1. Grid parameters: `io.dlnE()` [Grid spacing in ln-space], `io.NLepE()` [number of electron grid points], `io.NLepG()` [number of photon grid points], `io.NHad()` [number of hadronic grid points], `io.NNU()` [number of neutrino grid points] 
    2. Grids in eV: `io.E_LepE_eV()` [array of electron grid], `io.E_LepG_eV()` [array of photon grid], `io.E_Had_eV()` [array of hadronic grid], `io.E_Nu_eV()` [array of neutrino grid]
    3. For conversion of energy in eV to gridpoint, users may rely on `io.EeV2i_LepE()` / `io.EeV2i_LepG()` / `io.EeV2i_Had()` / `io.EeV2i_Nu()`

In contrast to the energy grid, the time step may be adjusted dynamically and is accessible through the parameter "dt" of the class RunParams, thus `rp.dt` (in s). 

## Source parameters

AM3 pre-assumes homogeneous particle distributions and magnetic fields. The source parameters can be printed out using `rp.PrintParams()`.

- The *magnetic field* is set through `rp.B_co` [G]. If you change it during run-time, call `sim.Update_B()` to re-calculate the kernels for magnetic field - dependant processes such as synchrotron emission
- For an expanding source, the *expansion timescale is set through `rp.t_expansion` [s].
- The *escape timescale* is set through `rp.t_esc` [s]. For each particle species, the escape time can be adjusted to a fraction of this, using the pattern
    > rp.FRAC\_esc\_ + \${Internal name} 
    Where the internal names are specified below. Important: Neutrinos, muons and pions are treated collectively, using `rp.FRAC_esc_HadNU`, `rp.FRAC_esc_HadMu` and `rp.FRAC_esc_HadPi`, respectively.
    
## Particle species

The code calculates the time-dependent evolution of the following species:

|Particle                   |Symbol             |Internal name  |
| -------------             | ---------         | -----------   |
| Electrons                 | $e^-$             | LepE          |
| Positrons                 | $e^+$             | LepP          |
| Photons                   | $\gamma$          | LepG          |
| Protons                   | $p$               | HadP          |
| Neutrons                  | $n$               | HadN          |
| Left-handed muons         | $\mu^-_L$         | MmL           |
| Right-handed muons        | $\mu^-_R$         | MmR           |
| Left-handed anti-muons    | $\mu^+_L$         | MpL           |
| Right-handed anti-muons   | $\mu^+_R$         | MpR           |
| Positive pions            | $\pi^+$           | Pip           |
| Negatie pions             | $\pi^-$           | Pim           |
| Muon neutrinos            | $\nu_{\mu}$       | Num           |
| Muon anti-neutrinos       | $\bar{\nu}_\mu$   | NumA          |
| Electon neutrinos         | $\nu_e$           | Nue           |
| Election anti-neutrinos   | $\bar{\nu}_e$     | NueA          |

### Accessing the particle distributions

Access is implemented through the IO class (with corresponding object io):

* The particle species can be accessed through get/set functions: \
    The scheme for getters is 

    > io.Edn\_dE\_ + \${Internal name} + () 
    
    For example `io.Edn_dE_LepE()`. For setting with an array input_array use

    > io.set_Edn\_dE\_ + \${Internal name} + (input\_array) 

    For example `io.set_Edn_dE_LepE(input_array)`. 
    Units are 1/cm$^3$ for all.
* Collecting *all* particles of a species: \
    Neutrinos may be read out as all-flavour array through `io.Edn_dE_Nu()`, 
    the summed distributions of positrons and electrons through `io.Edn_dE_LepEP()`,
    the summed distributions of all muons through `io.Edn_dE_Mu()` and 
    the summed distributions of positive and negative pions through `io.Edn_dE_Pipm()`.
* Photons by emitting process: Photons can be separated by the physics process they originate from. \
    If they are generated by a secondary electron/positron population, the pattern is

    > io.Edn\_dE\_LepG\_ + \${Process abbreviation} + \${sy/ic/syic}

    The process abbreviations are introduced [below](#physics-processes), in addition primary (injected) electrons have the process abbreviation 'in'. 
    \${sy/ic/syic} specifies whether the photons are due to [synchrotron/inverse Compton/synchrotron and inverse Compton radiation] of the leptons.
    Thus, the command finally may read for example `io.Edn_dE_LepG_bhsy()` or `io.Edn_dE_LepG_insy()`. \
    Synchrotron and inverse Compton radiation from pions, muons and protons are accessed through

    > io.Edn\_dE\_LepG\_ + \${particle abbreviation} + \${sy/ic/syic}

    Here, the particle abbreviations are 'pi' for pions, 'mu' for muons and 'p' for protons, yielding for example `io.Edn_dE_LepG_psy()` for proton synchrotron radiation. \ 
    Finally, Photons from $\pi^0$ decays are accessed through  `io.Edn_dE_LepG_pi0()`.
* Secondary leptons by generating process: Secondary lepton pairs may be accessed in a similar pattern as photons, thus

    > io.Edn\_dE\_LepEP\_ + \${Process abbreviation}

    For example `io.Edn_dE_LepEP_pg()`. Here we again use the process abbreviations (bh/pair/pg) introduced [below](#physics-processes) and 'in' for (internally) injected leptons. 

## Physics processes

The following physics processes are included: 

|Process                        |Abbreviation   | Terms entering the differential equations                             |
|--------                       | ------------  | ------------------------------                                        |   
|Synchrotron                    | sy            | $Q_\gamma$, $\alpha_\gamma$, $\dot{E}$ for all charged particles      |
|Inverse Compton                | ic            | $Q_\gamma$, $\alpha_\gamma$, $\dot{E}$ for all charged particles      |
|$\gamma \gamma$ annihilation   | pair          | $\alpha_\gamma$, $Q_{e^{\pm}}$                                        |
|Photo-pair production          | bh            | $\dot{E}_p$, $Q_{e^{\pm}}$                                            |
|Photo-pion production          | pg            | $\alpha_{\gamma}$, $\alpha_p$, $Q_{\pi^\pm}$, $Q_\gamma$              |
|Adiabatic expansion            | ad            | $\alpha$ for all particles, $\dot{E}$ for all charged particles       |
|Escape                         | es            | $\alpha$ for all particles                                            |
|Pion decay                     | dec           | $\alpha_{\pi^\pm}$, $Q_{\mu^\pm}$, $Q_{\nu_\mu}$                      |
|Muon decay                     | dec           | $\alpha_{\mu^\pm}$, $Q_{e^\pm}$, $Q_{\nu_\mu}$, $Q_{\nu_e}$           |
|Injection                      | inj           | $Q_{e^{-}}$, $Q_p$                                                    |

**Notes**: (1) Due to their short lifetime, neutral pions are assumed to decay instantaneously. For photo-pion production we hence don't list a source term for neutral pions but instead a photon source term. (2) Injection here refers to the build-in injection. Arbitrary injection is possible by passing arrays. 

For details on the implementation of the different processes we point to [Gao et al - new paper placeholder].


### Accessing timescales

Particle timescales (in s) can be accessed through  

> io.t\_ + \${Particle internal name} + \_ + \${Process abbreviation}

For example `io.t_LepE_sy()`. \
In addition to the processes listed above it is possible to retrieve the acceleration timescale for electrons and protons. It is defined as 

$$ t^{-1}_\mathrm{acc} (\gamma) = \frac{\eta e B}{m c \gamma} $$

for a particle of Lorentz factor $\gamma$, mass $m$, electric charge $e$ in a magnetic field $B$. The acceleration efficiency $\eta$ can be set through `rp.eta_Bohm_Lep` (for leptons) and `rp.eta_Bohm_Had` (for hadrons). From this, code-internally also the maximum energy can be determined, balancing losses and acceleration, using `sim.Estimate_MaximumLeptonEnergy()` and `sim.Estimate_MaximumProtonEnergy()`.

### Injection of arbitrary distributions

Arbitrary particle distributions may be injected by passing an input_array (in 1/cm$^3$s) to AM3, following the pattern

> io.set\_Edn\_dEdt\_ext\_ + \${Particle internal name} + (input_array)

For example `io.set_Edn_dEdt_ext_HadP(input_array)`. Please ensure before that the array size is correct, no internal checks are implemented! \
The corresponding get-functions follow the pattern 

> io.Edn\_dEdt\_ext\_ + \${Particle internal name}

For example `io.Edn_dEdt_ext_HadP()`.

### Internal injection 

The internal injection arrays are accessed through

> io.Edn\_dEdt\_int\_ + \${Particle internal name}

For example `io.Edn_dEdt_int_HadP()`. \
Three different shapes can be selected for pre-implemented internal injection: 
1. Mono-energetic injection: 
    $$ Q(\gamma) = \begin{cases} C \, , $\gamma_\mathrm{min} < \gamma < \gamma_\mathrm{max} \\
                                0 \, else \end{cases} $$ 
2. Power-law injection:
    $$ Q(\gamma) = \begin{cases} C \gamma^{-p} \mathrm{exp}(A_\mathrm{cutoff}\gamma/ \gamma_\mathrm{max})\, , $\gamma_\mathrm{min} < \gamma  \\
                                0 \, else \end{cases} $$ 
3. Power-law injection:
    $$ Q(\gamma) = \begin{cases} C_1 \gamma^{-p_1} \, , $\gamma_\mathrm{min} < \gamma  < $\gamma_\mathrm{break}\\
                    C_2 \gamma^{-p_2} \mathrm{exp}(A_\mathrm{cutoff} \gamma/ \gamma_\mathrm{max})\, , $\gamma_\mathrm{break} < \gamma  \\
                                0 \, else \end{cases} $$ 
The parameters for the internal injection are stored in the `RunParams` class. For an object `rp` of that class, specify the total injection power density through `rp.p_in` [erg/cm$^3$s]. Then, `rp.FRACe` and `rp.FRACp` specify the fraction of that power density passed to electrons and protons. From this the normalisation constants are calculated. \
The power-law indices and maximum/minimum/break energies are adjusted as follows:
- Electrons: Use `rp.e_inj_Emin_eV`, `rp.e_inj_Emax_eV`, `rp.e_inj_Emin_eV` to specify the minimum, maximum and break energy (all in eV). Then `rp.e_inj_index` is the power-law index for power-law injection (or the low-energy index for broken power-law injection), `rp.e_inj_index_high` is the high-energy power-law index and `rp.e_inj_cutoff_steepness` the steepness of the exponential power-law cutoff ($A_\mathrm{cutoff}$ above).
- Protons: Use `rp.p_inj_Emin_eV`, `rp.p_inj_Emax_eV`, `rp.p_inj_Emin_eV` to specify the minimum, maximum and break energy (all in eV). Then `rp.p_inj_index` is the power-law index for power-law injection (or the low-energy index for broken power-law injection), `rp.p_inj_index_high` is the high-energy power-law index and `rp.p_inj_cutoff_steepness` the steepness of the exponential power-law cutoff ($A_\mathrm{cutoff}$ above).

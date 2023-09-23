# Code overview

AM3 solves the time-dependent 

## Code structure

The user-interface module is split in a few classes:
  * io holds the input/output options
  * sim is the core class holding a single simulation
  * ph is the physics manager, a helper class to collect all physics processes. It does not have to be accessed, only initialisation is required.
  * rp holds the parameters of the simulation, such as the source details.

## Run settings: Grids

Code-internal we differentiate between three energy grids: The lepton ($e^\pm$), photon ($\gamma$) and hadronic (all other particles) ones; all equally spaced in logarithmic space (base e). The grid settings are specified during compilation and thus cannot be changed during runtime. 
Grid parameters and access:
* *Definition of energy grids* is done in include/AM3/global_defs.h .
    Photon grid length is defined by BIN_X, photon grid origin X_I. The other grid lengths are derived: BIN_E = BIN_X + X_I, BIN_P = BIN_E - 26. Grid spacing D_X = 0.1 (in e base) should not be changed, it will lead to erroneous results
* *Readout of grids* is via class io:
    1. Grid parameters: `io.dlnE()` [Grid spacing in ln-space], `io.NLepE()` [number of electron grid points], `io.NLepG()` [number of photon grid points], `io.NHad()` [number of hadronic grid points], `io.NNU()` [number of neutrino grid points] 
    2. Grids in eV: `io.E_LepE_eV()` [array of electron grid], `io.E_LepG_eV()` [array of photon grid], `io.E_Had_eV()` [array of hadronic grid], `io.E_Nu_eV()` [array of neutrino grid]
    3. For conversion of energy in eV to gridpoint, users may rely on `io.EeV2i_LepE()` / `io.EeV2i_LepG()` / `io.EeV2i_Had()` / `io.EeV2i_Nu()`

In contrast to the energy grid, the time step may be adjusted dynamically and is accessible through the parameter `rp.dt` (in s). 

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
| Muon neutrinos            | $\nu_\mu$         | Num           |
| Muon anti-neutrinos       | $\bar{\nu}_\mu$   | NumA          |
| Electon neutrinos         | $\nu_e$           | Nue           |
| Election anti-neutrinos   | $\bar{\nu}_e$     | NueA          |

### Accessing the particle distributions

* The particle species can be accessed through get/set functions: 
    The scheme for getters is io.Edn_dE_[internal name]() (for example: `io.Edn_dE_LepE()`). For setting with an array input_array use io.set_Edn_dE_[internal name](input_array) (for example: `io.set_Edn_dE_LepE(input_array)`).
* Collecting *all* particles: 
* Photons by emitting process

## Source parameters

The class r


## Physics processes

The following physics processes are included: 

|Process                | Terms entering the differential equations                         |
|--------               | ------------------------------                                    |   
|Synchrotron            | $Q_\gamma$, $\alpha_\gamma$, $\dot{E}$ for all charged particles  |
|Inverse Compton        | $Q_\gamma$, $\alpha_\gamma$, $\dot{E}$ for all charged particles  |
|Photo-pair production  | $\dot{E}_p$, $Q_e^{\pm}$                                          |
|Photo-pion production  | $\alpha_\gamma$, $\alpha_p$, $Q_\pi^{\pm}$, $Q_\gamma$            |
|Adiabatic expansion    | $\alpha $ for all particles, $\dot{E}$ for all charged particles  |
|Escape                 | $\alpha $ for all particles                                       |
|Pion decay             | $\alpha_{\pi^\pm}$, $Q_{\mu^\pm}$, $Q_{\nu_\mu}$                  |
|Muon decay             | $\alpha_{\mu^\pm}$, $Q_{\e^\pm}$, $Q_{\nu_\mu}$, $Q_{\nu_e}$      |
|Injection              |$Q_{e^{-}}$, $Q_p$                                                 |

**Notes**: (1) Due to their short lifetime, neutral pions are assumed to decay instantaneously. We hence don't list a neutral pion but a photon source term for photo-pion production. (2) Injection here refers to the build-in injection. Arbitrary injection is possible by passing arrays. 

### Accessing timescales
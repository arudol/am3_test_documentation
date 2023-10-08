# Running AM3

Here we provide a brief(!) overview of the different steps neccessary to set up and run a simulation in AM3. We recommend looking at the Quickstart and the Detailed example to gain more intuition on how to use AM3, explaining also how read-out and plotting work.

### Import the library

```python
import pybind_AM3 as am3
```

### Initialize the data arrays and source parameters class

```python
dat = am3.AM3Arrays()
rp = am3.RunParams()
```

### Set the source parameters

```python

rp.e_inj_Emin_eV = 1.e4
rp.e_inj_Emax_eV = 1.e6
rp.e_inj_index = 2.0

rp.p_in = 1.e44 #erg/s/cm3
rp.FRACe = 0.5
rp.FRACp = 0.0
rp.dt = 1.e-3 * 1.e16/3.e10
rp.B_co = 0.1
rp.t_esc = 1.e16/3.e10

```

### Intialize Physics Handler, Simulation manager and InputOutput

``` python
ph = am3.PhysicsHandler(rp, dat)
sim= am3.SimulationManager(rp, ph)
io = am3.IO(sim, rp, dat)
```

### Adjust the processes using switches 

```python

sim.process_in = 1 # internal injection: ON
sim.internal_inj_type = 1 #internal injection type: 1= power-law

sim.process_esy = 1 # electron synchrotron: ON

sim.process_eic = 1 # electron inverse Compton: ON

sim.process_pair = 0 # gamma-gamma annihilation: OFF

sim.process_es = 1 # escape: ON
sim.escape_type = 1 # escape type: 1 = free-streaming for all particles

sim.process_adi = 0 # adiabatic cooling: OFF
sim.process_exp = 0 # volume expansion term: OFF

sim.process_parse_sed = 1
```

### Initialise Kernels and clear particles

```python
sim.InitKernels()
sim.Clear_Particles()
```

### Evolve one timestep

```python
sim.EvolveStep()
```

# Installation

AM3 can be installed either through docker or by compiling the code yourself. 
Here we describe how to run compile the code yourself and import it into python,
for [this page](sec_run_with_docker) for running using docker or [this page](sec_run_with_c++)  for running directly in C++.

Due to library dependencies we stronlgy recommend compiling and using in the same environment! 
This implies *(a)* compiling on the machine (or laptop) that you want to use it on, ideally *(b)* also in the same python environment. 
The latter can be realised by creating a fixed conda environment 

## Prerequisites:

1. python3
    - pybind11: install e.g. through conda `sudo conda install pybind11`

2. g++
    - gsl library: install e.g. through your standard package manager (apt/dnf/...) e.g. using apt: `sudo apt install libgsl-dev`

3. make

## Making AM3:

1. Adjust the paths in the makefile

    ````
    PYTHON_BASE = $(shell python -c "import sys; print(sys.base_prefix)")
    PATH_TO_PYTHONLIB = $(PYTHON_BASE)/lib
    PYTHONROOT = $(PYTHON_BASE)/include/python3.7m

    ````
    
2. Run `make` to compile and link AM3. This will create the library
    in the relative folder  `libpython/lib/pybind_core.so`


## Importing the library in python:

In order to use the library add its path `$YOUR_PATH_TO_AM3/libpython/lib` (where `$YOUR_PATH_TO_AM3` should be replaced with the path where you store AM3) to your `PYTHONPATH`. This can be done by running in a terminal

```bash
export PYTHONPATH="$YOUR_PATH_TO_AM3/libpython/lib"
```
To add it *permanently* to you python path, adding the above line to the end of your `~/.bashrc` file (if you are on linux and using bash), or to the end of your `~/.bash_profile` (if you ar on OS). \
Alternatively, you can simply link to it during your python run, by adding

```python
import sys
sys.path.append($YOUR_PATH_TO_AM3/libpython/lib)
```
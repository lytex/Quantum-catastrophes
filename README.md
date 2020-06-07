# Quantum-catastrophes
Python code for "Emergence of singularities from decoherence: Quantum catastrophes" (not author's code)

# Usage
The project uses [pip-tools](https://pypi.org/project/pip-tools/) to manage dependencies.

* First try `pip install -r requirements.in` to get the latest version of each package
* If that fails, `pip install -r requirements.txt` to install from a requirements.txt with specific versions
  that are guaranteed to work
* **If the scripts won't work because of uncompatibility regarding non-ASCII characters,
  you can use the ascii_... versions**

# Video
* To generate videos, you have to install `ffmpeg` and adding it to PATH (or use a different [FileWriter](https://matplotlib.org/3.2.1/api/animation_api.html))

## classical.py
Generates figures 1 and 5 (classical)
* You can tweak the parameters in `Model and computational constants` and `Visualization and video options` 
* Select which figure/video you want to generate by setting `option` to be one of:
```
    "FIG. 5 Phase space video",
    "Rainbow phase space video",
    "FIG. 1 TWA trajectories"
```
### Parameters for Fig. 1a
```
    Λ = 25
    ΔE = 0
    GRIDSIZE = 50
    t_max = 3.5
    Δt = 0.01
```
### Parameters for Fig. 6
```
    Λ = 25
    ΔE = 1
    GRIDSIZE = 50
    t_max = 3.5
    Δt = 0.01
```

## quantum.py
### Parameters for Fig. 1b
```
    MAX_J = 50
    Λ = 25
    ΔE = 0
    N = 100
    D = 0.0
    t_max = 3.5
    Δt = 0.01
```
### Parameters for Fig. 1c
```
    MAX_J = 50
    Λ = 25
    ΔE = 0
    N = 100
    D = 0.1
    t_max = 6
    Δt = 0.01
```

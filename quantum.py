from qutip import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, writers
import matplotlib as mpl

MAX_J = 50
Λ = 25
ΔE = 0
N = 100
D = 0.0

t_max = 3.5
Δt = 0.01

t_max = np.pi * t_max / np.sqrt(1 + Λ)  # Normalization
Δt = np.pi * Δt / np.sqrt(1 + Λ)
t = np.arange(0, t_max, Δt)

Jx = jmat(MAX_J, "x")
Jz = jmat(MAX_J, "z")
z = np.linspace(-2 * MAX_J / N, +2 * MAX_J / N, 2 * MAX_J + 1) / (
    2 / np.sqrt(Λ)
)  # Normalization

H = Λ / N * Jz ** 2 - Jx + ΔE * Jz

ρ0 = spin_state(MAX_J, 0, type="dm")

measure = np.sqrt(D * Λ / N) * Jz

solution = mesolve(H, ρ0, t, c_ops=measure)
ρ = solution.states

ρ_zz = np.array([x.diag() for x in ρ])

ρ_zz[ρ_zz < 0] = 0

t = np.sqrt(1 + Λ) * t / np.pi
zv, tv = np.meshgrid(z, t)

scale = {"vmin": 0, "vmax": 0.2, "levels": 999}
fig, ax = plt.subplots(1, 1, figsize=(7, 6))
cf = ax.contourf(zv, tv, ρ_zz, cmap=plt.get_cmap("plasma"), antialiased=False,
    levels=np.linspace(0, 0.2, 1000))
ax.axis((-1.25, 1.25, t.min(), t.max()))
fig.colorbar(cf, ax=ax, ticks=[0, 0.05, 0.1, 0.15, 0.2], extend="both")
plt.draw()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, writers
from scipy.integrate import solve_ivp


def ClassicalBJJEnsemble(Λ, ΔE, size):
    def f(t, v):
        z, ϕ = v[slice(0, size)], v[slice(size, None)]
        val = np.hstack(
            [
                -np.sqrt(1 - z ** 2) * np.sin(ϕ),
                Λ * z + z / np.sqrt(1 - z ** 2) * np.cos(ϕ) + ΔE,
            ]
        )
        return val

    return f


def solve(Λ, ΔE, gridsize=1000, t_max=20, Δt=0.1):

    ϕ = np.linspace(-np.pi, np.pi, gridsize)
    z = np.zeros_like(ϕ)
    f = ClassicalBJJEnsemble(Λ, ΔE, len(z))
    t_max = np.pi * t_max / np.sqrt(1 + Λ)  # Normalization
    Δt = np.pi * Δt / np.sqrt(1 + Λ)

    solution = solve_ivp(f, [0, t_max], np.hstack((z, ϕ)), max_step=Δt)

    z, ϕ = solution.y[slice(0, len(z))].T, solution.y[slice(len(z), None)].T
    z = z / (2 / np.sqrt(Λ))  # Normalization
    t = solution.t

    return z, ϕ, t



def animate(i):
    scat.set_offsets(np.array([ϕ[i], z[i]]).T)
    scat.set_sizes(np.ones_like(ϕ[i]))


if __name__ == "__main__":


    ################## Model and computational constants #######################
    Λ = 25
    ΔE = 0
    GRIDSIZE = 100000
    t_max = 50
    Δt = 0.1

    ################### Visualization and video options ########################
    interframe_interval = 20
    video_file = 'vid/Test.mp4' # False means no video is produced
    video_duration_seconds = 30 # 

    option = "FIG. 5 Phase space video"

    options = (
        "FIG. 5 Phase space video",
        "Rainbow phase space video",
        "FIG. 1 TWA trajectories",
    )

    if option == "Rainbow phase space video":
        rainbow = True
    else:
        rainbow = False


    z, ϕ, t = solve(Λ, ΔE, GRIDSIZE, t_max, Δt)

    if option in ["FIG. 5 Phase space video", "Rainbow phase space video"]:

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set(xlim=(-np.pi, np.pi), ylim=(z.min(), z.max()))
        if rainbow:
            cmap = plt.get_cmap("gist_rainbow")(np.linspace(0, 1, GRIDSIZE))[:, :3]
            scat = ax.scatter(x=ϕ[0], y=z[0], s=1, c=cmap)
            anim = FuncAnimation(fig, animate, interval=interframe_interval, frames=len(t) - 1)
        else:
            scat = ax.scatter(x=ϕ[0], y=z[0], s=1, c='b')
            anim = FuncAnimation(fig, animate, interval=interframe_interval, frames=len(t) - 1)
        if video_file:
            Writer = writers['ffmpeg_file']
            fps = len(t)/video_duration_seconds 
            fps = fps if fps > 25.0 else 25.0 # Minumum of 25fps
            writer = Writer(fps=fps)
            anim = FuncAnimation(fig, animate, frames=len(t) - 1, repeat=False, cache_frame_data=False)
            anim.save(video_file, writer=writer)
        else:
            plt.draw()
            plt.show()


    if option == options[1]:
        plt.figure(figsize=(7, 6))
        plt.plot(z, t, "b-", lw=1)
        plt.axis((z.min(), z.max(), t.min(), t.max()))
        plt.show()

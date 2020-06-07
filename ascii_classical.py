import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, writers
from scipy.integrate import solve_ivp


def ClassicalBJJEnsemble(Lambda, dE, size):
    def f(t, v):
        z, phi = v[slice(0, size)], v[slice(size, None)]
        val = np.hstack(
            [
                -np.sqrt(1 - z ** 2) * np.sin(phi),
                Lambda * z + z / np.sqrt(1 - z ** 2) * np.cos(phi) + dE,
            ]
        )
        return val

    return f


def solve(Lambda, dE, gridsize=1000, t_max=20, dt=0.1):

    phi = np.linspace(-np.pi, np.pi, gridsize)
    z = np.zeros_like(phi)
    f = ClassicalBJJEnsemble(Lambda, dE, len(z))
    t_max = np.pi * t_max / np.sqrt(1 + Lambda)  # Normalization
    dt = np.pi * dt / np.sqrt(1 + Lambda)

    solution = solve_ivp(f, [0, t_max], np.hstack((z, phi)), max_step=dt)

    z, phi = solution.y[slice(0, len(z))].T, solution.y[slice(len(z), None)].T
    z = z / (2 / np.sqrt(Lambda))  # Normalization
    t = solution.t

    return z, phi, t



def animate(i):
    scat.set_offsets(np.array([phi[i], z[i]]).T)
    scat.set_sizes(np.ones_like(phi[i]))


if __name__ == "__main__":


    ################## Model and computational constants #######################
    Lambda = 25
    dE = 0
    GRIDSIZE = 50
    t_max = 3.5
    dt = 0.01

    ################### Visualization and video options ########################
    interframe_interval = 20
    video_file = False # False means no video is produced
    video_duration_seconds = 30 # 

    option = "FIG. 1 TWA trajectories"

    options = (
        "FIG. 5 Phase space video",
        "Rainbow phase space video",
        "FIG. 1 TWA trajectories",
    )

    if option == "Rainbow phase space video":
        rainbow = True
    else:
        rainbow = False


    z, phi, t = solve(Lambda, dE, GRIDSIZE, t_max, dt)

    if option in ["FIG. 5 Phase space video", "Rainbow phase space video"]:

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.set(xlim=(-np.pi, np.pi), ylim=(z.min(), z.max()))
        if rainbow:
            cmap = plt.get_cmap("gist_rainbow")(np.linspace(0, 1, GRIDSIZE))[:, :3]
            scat = ax.scatter(x=phi[0], y=z[0], s=1, c=cmap)
            anim = FuncAnimation(fig, animate, interval=interframe_interval, frames=len(t) - 1)
        else:
            scat = ax.scatter(x=phi[0], y=z[0], s=1, c='b')
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


    if option == "FIG. 1 TWA trajectories":
        plt.figure(figsize=(7, 6))
        plt.plot(z, t, "b-", lw=1)
        plt.axis((z.min(), z.max(), t.min(), t.max()))
        plt.show()

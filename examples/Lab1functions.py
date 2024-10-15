import numpy as np
import matplotlib.pyplot as plt
from lab01 import (
    launch_angle_range,
    launch_angle,
    arcsin,
)


def main():
    """ The function that takes the constant value inputs,
     calls the functions from func01, and produces calculated plots and arrays.
     -------
     Parameters:
         (None,
         )
     -----
     Returns:
           (None,
           )

     """
    ve_v0 = 2.0  # for when kept constant
    alpha = 0.25  # for when kept constant
    tol_alpha = 0.04  # for when kept constant

    launch_angle_range(ve_v0, alpha, tol_alpha)

    # Define range for ve_v0
    rng_ve_v0 = np.linspace(1.4, 2.0, 100)

    min_ve_v0 = []
    max_ve_v0 = []

    for ve_v0 in rng_ve_v0:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_ve_v0.append(phi_range[0])
        max_ve_v0.append(phi_range[1])

    plt.figure(figsize=(10, 6))
    plt.plot(rng_ve_v0, min_ve_v0, label="Min. Launch Angle", linewidth=1, color="cyan")
    plt.plot(rng_ve_v0, max_ve_v0, label="Max. Launch Angle", linewidth=1, color="magenta")
    plt.xlabel("Ve/v0")
    plt.ylabel("Launch angle in rad")
    plt.title("Launch Angle with respect to a range of ve_v0")
    plt.legend(title="Legend", alignment="left")
    plt.grid()
    plt.savefig('C:\\users\\zcmit\\git\\goph419projects\\goph419_f2024_lab01_stZM\\figures\\launch_angle_rangeplotsVE_V0.png')
    plt.show()

    # Define range for alpha
    rng_alpha = np.linspace(0.01, 0.04, 100)

    min_angle = []
    max_angle = []

    for alpha in rng_alpha:
        phi_range = launch_angle_range(ve_v0, alpha, tol_alpha)
        min_angle.append(phi_range[0])
        max_angle.append(phi_range[1])

    plt.figure(figsize=(10, 6))
    plt.plot(rng_alpha, min_angle, label="Min Launch Angle", linewidth=1, color= "blue")
    plt.plot(rng_alpha, max_angle, label="Max Launch Angle", linewidth=1, color="green")
    plt.xlabel("Alpha (m)")
    plt.ylabel("Launch angle in rad")
    plt.title("Launch Angle with respect to alpha")
    plt.legend(title="Legend", alignment="left")
    plt.grid()
    plt.savefig(
        'C:\\users\\zcmit\\git\\goph419projects\\goph419_f2024_lab01_stZM\\figures\\launch_angle_rangeplotsALPHA.png')
    plt.show()


if __name__ == "__main__":
    main()





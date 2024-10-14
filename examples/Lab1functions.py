import numpy as np
import matplotlib.pyplot as plt
from lab01 import (
    launch_angle_range,
    launch_angle,
    arcsin,

)

earthrad = 6378


def main():
    ve_v0 = 2.0  # for when kept constant
    alpha = 0.25  # for when kept constant
    tol_alpha = 0.04  # for when kept constant

    launch_angle_range(ve_v0, alpha, tol_alpha)

# numpy linespace for ve_v0 range
    rng_ve_v0 = np.linspace(1.4, 2.0, 100)
    # plot that hold ve_v0 constant
    xpoints = alpha
    ypoints = launch_angle_range(ve_v0, alpha, tol_alpha)
    plt.plot(xpoints, ypoints)
    plt.show()




if __name__ == "__main__":
    main()








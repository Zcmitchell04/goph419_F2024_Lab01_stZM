import numpy as np
from lab01 import (
    launch_angle_range,
    launch_angle,
    arcsin,

)

earthrad = 6378


def main():
    ve_v0 = 1.0 # input
    alpha = 0.25
    tol_alpha = 0.02

    launch_angle_range(ve_v0, alpha, tol_alpha)




if __name__ == "__main__":
    main()








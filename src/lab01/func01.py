import numpy as np
import math

# defining constant variables
""" defining my constant variables
    earthrad = radius of Earth
    earthmass = mass of Earth
    gravcons = Gravitational constant
    launchmass = mass of launch vehicle
    distearth = distance of vehicle to centre of earth
"""

# function that takes the ratio of escape velocity to terminal velocity

earthrad = 6378
earthmass = 5.972E24
gravcons = 6.67430E-11


def arcsin(x):
    """Function for equation 18

    parameters:

    x: the right hand side of eq. 18

    """
    if -1 < x < 1:
        raise ValueError(f"Invalid x value: {x}")
    result = 0.0
    eps_a = 1.0
    tol = 1.0e-8 #error tolerance
    n = 1
    fact_n = math.factorial(n)
    fact_2n = math.factorial(n*2)
    n_max = 100
    while eps_a > tol and n < n_max:
        dy = ((2 * x) ** (2 * n)) / ((n**2)*(fact_2n/(fact_n**2)))
        result += dy
        n += 1
        eps_a = abs(dy/ result)
        sininv = np.sqrt(0.5*(result))
        return(sininv)






def launch_angle(ve_v0, alpha):
    """The function for equation 17
    
    parameters:
    ve_v0 : the input ratio of escape and terminal velocity
    alpha: desired max. alt as a fraction of earht's radius
    
    """
    if ve_v0 < 0 or alpha < 0:
        raise ValueError(f"Invalid ve_v0 or alpha value: {ve_v0} or {alpha}")
    sin0 = (1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * (ve_v0 ** 2)))  #eq 17
    result = arcsin(sin0)
    return result



def launch_angle_range(ve_v0, alpha, tol_alpha):
    """Description of function.
    Parameters:
        ve_v0: the input ratio of escape and terminal velocity
        alpha: desired max. alt. as a fraction of earth's radius
        tol_alpha: tolerance of max alt.
    ----------
    Returns
    -------
    """

    # create a two-component array in numpy that shows:
    # minimum allowable launch angle (when max = (1 + tol_alpha)*alpha)
    # maximum allowable launch angle (when max = (1-tol_alpha)*alpha)

    # compute the inverse sin such that at least 5 sig figs are correct


# implementation of Equations (17) and (18)
# ...
    array_list = []

    posmax_alt = ((1 + tol_alpha) * alpha)  # max allowable launch angle: corresponds to highest altitude
    array_list.append(launch_angle(ve_v0, posmax_alt))

    negmax_alt = ((1 - tol_alpha) * alpha)  # min allowable launch angle: corresponds to the lowest altitude
    array_list.append(launch_angle(ve_v0, negmax_alt))

    phi_range = np.array(array_list)

    print(phi_range)



















###Practice implementation:

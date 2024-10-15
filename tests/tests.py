
import numpy as np
from lab01 import (
    launch_angle_range,
    launch_angle,
    arcsin,

)

#both ve_v0 and alpha should be above 0
def test_arcsin():
    # takes the argument "x"
    tol = 1.0E-8
    x = 0.6  # -1 < x < 1

    print("now testing the arcsin function: ")
    result = arcsin(x)
    expected = np.asin(x)

    # Comparing the values:
    if np.abs((result - expected) / expected) < tol:
        print(f"PASSED, result value {result} and expected value {expected} agree.")
    else:
        print(f"FAILED: expected calculation was {expected} but got {result}.")




def test_launch_angle():
    # takes inputs of "alpha" and "ve_v0"
    tol = 1.0E-8
    ve_v0 = 2.0
    alpha = 0.2
    print(f"now testing the launch_angle function: finding result for ve_v0 value {ve_v0} and alpha value {alpha}")

    # what's expected
    sin0 = ((1 + alpha) * (np.sqrt(1 - (alpha / (1 + alpha)) * ve_v0 ** 2)))  # eq 17
    expected = np.asin(sin0)

    # what's calculated
    result = launch_angle(ve_v0, alpha)


    if np.abs((result - expected) / expected) < tol:
        print(f"PASSED, result value {result} and expected value {expected} agree.")
    else:
        print(f"FAILED: expected calculation was {expected} but got {result}.")


def test_launch_angle_range():
    # takes inputs of "alpha", "ve_v0" and "tol_alpha"
    ve_v0 = 2.0  # input
    alpha = 0.25
    tol_alpha = 0.04
    print(f"now testing the launch_angle_range function: finding result for alpha value {alpha}, ve_v0 value {ve_v0}, and tol_alpha value {tol_alpha}")

    # using numpy functions to calc. expected values:
    expected_values_list = []
    posmax_alt = ((1 + tol_alpha) * alpha)
    expected_list = expected_values_list.append((launch_angle(ve_v0, posmax_alt)))
    negmax_alt = ((1 - tol_alpha) * alpha)
    expected_list = expected_values_list.append(launch_angle(ve_v0, negmax_alt))
    expected_range = np.array(expected_list)

    # using my function to calc. resulting values:
    result = launch_angle_range(ve_v0, alpha, tol_alpha)
    actualresult = np.array(result)

    # comparing the two:
    if np.array_equal(result, expected_values_list):
        print(f"PASSED, result range {expected_list} and expected range {actualresult} agree.")
    else:
        print(f"FAILED: expected calculation was {expected_list} but got {actualresult}.")


if __name__ == "__main__":
    test_arcsin(), test_launch_angle(), test_launch_angle_range()

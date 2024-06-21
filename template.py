#!/usr/bin/env python3
#encode: utf8

"""
@file       template.py
@copyright  InSolem SARL reserves all rights even in the event of industrial
            property rights. We reserve all rights of disposal such as
            copying and passing on to third parties.


@brief      Here is a short description of the purpose of this module.
@details    This module is just a template of how should look like a python file
            according to the coding rules defined at InSolem SARL.

@note       If statements
            # Allowed
            if (logicalVariable == True):
            if (logicalVariable == False) and (number > 0):
            if (mayBeNone is None):
            if (mayBeNone is not None):

            # Not allowed
            if (logicalVariable):
            if (not logicalVariable):
            if (not logicalVariable) and (number):
            if (mayBeNone != None):
            if (mayBeNone):

@note       # Allowed
            import pyserial
            import matplotlib.pyplot as plt
            from Qt5 import QThread, Qpanel

            # Discouraged
            from maths import *
"""

# Constants
DEV_SENSOR_1 = "/dev/ttySUB0"
PI = 3.1416
FILTER_ENABLED = False


class MyClass:
    """
    Doc of the class
    """

    def MyFirstFunction(firstInput, secondInput):
        """
        Doc of the function
        """
        return firstOutput, secondOutput


def Function(distance, temps, sensors, startIdx=0, path=None):
    """
    @brief    Dummy function to demonstrate how the documentation should be
              written. Implements ALOA algorithm from Kenvic et al, "Fast Converging
              Stable Algorithm for Sun Temperature Matching", 2019, NGIST Journal.

    @param    distance  Distance [m] from the target.
    @param    temps     Ndarray of NxM temperatures [Celsius] where M is the number of thermometers sensors
                        and N the number of samples.
    @param    sensors   List of M TempSensors objects handling each thermometer.
    @param    startIdx  Index of the first thermometer to use in the list of sensors.
    @param    path      Path of CSV file where to save the data.


    @return   Returns a tuple (mean, fileDes, vars) where mean is the mean of all temperature [Celsius]
              fileDes is the the file descriptor (as an integer) where the data was saved, and vars is
              a Nx1 ndarray with the variance across all sensors for each temperature sample [Celsius^2]
    """
    ...
    return mean, fileDes, vars


def FindCommonRoots(polynom1, polynom2, resolution=0.01, method="Fibonacci"):
    """
    @brief    function that should calculate the roots of two given polynoms

    @param      polynom1    First referenced polynomial
    @param      polynom2    Second referenced polynomial
    @param      resolution  Parameter to define the resolution of the calculated roots.
    @param      method      Specifies the method to use for the calculation.

    @return     Returns a tuple of the found roots.

    @warning    This function is still not implemented
    """
    pass



if __name__ == "__main__":
    # Called only when this module is run as a script
    # Do the main work or embeds unit tests.

    poly1 = (1,4,2)
    poly2 = (2,1,2)

    # Allowed
    roots = FindCommonRoots(poly1, poly2, method="Fibonacci")
    roots = FindCommonRoots(poly1, poly2, method="Levenberg", resolution=0.5)

    # Not allowed
    roots = FindCommonRoots(poly1, poly2, "Fibonacci")
    roots = FindCommonRoots(poly1, method="Fibonacci", poly2)
    roots = FindCommonRoots(poly1, poly2, method = "Levenberg", resolution = 0.5)
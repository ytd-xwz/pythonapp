#!/usr/bin/env python3
#--coding: UTF-8--

"""
@file       graph_code.py
@copyright  InSolem SARL reserves all rights even in the event of industrial
            property rights. We reserve all rights of disposal such as
            copying and passing on to third parties.
"""

import numpy as np                      # import the numpy library and rename it np
from matplotlib import pyplot as plt    # import from the matplotlib library the fonction pyplot and rename it plt

## init
#plt.clf()                   # erase the old charts
#plt.title('la base')        # add a title to the graph
#plt.show()                  # show the chart
#plt.xlabel('x')             # name the x axis "x"
#plt.ylabel('y')             # name the y axis "y"
#plt.grid()                  # add a grid to the chart
#
#def fonction():
#
#    
#
#
#
#plt.plot(fonction)




plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def f(x):
   return np.sin(x)*x/x*x

x = np.linspace(-1000, 1000, 1000)

plt.plot(x, f(x), color='blue')
plt.grid()
plt.show()
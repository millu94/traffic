import numpy as np
import matplotlib.pyplot as plt
import math

# array of arbitrary zeros and ones
traffic_model = [0, 1, 0, 1, 1, 0, 0, 1, 0, 0]

plt.imshow()

"""

iterate through all the cells and apply the following set of rules per
iteration:

if the value of a cell is 1 ( if c_n(j) == 1 )
    if the value in front of that cell is 1 ( if c_n(j+ 1) == 1 )
        then the value of the cell in the next iteration is 1
        ( c_n+1(j) == 1 )
    else, the value of the cell in the next iteration is 0
    ( c_n+1(j) == 0 )
else, if the value of a cell is zero ( if c_n(j) == 0 )
    if the value behind that cell is 1 ( if c_n(j-1) == 1)
        then the value of the cell in the next iteration is 1
        ( c_n+1(j) == 1 )
    else, the value of the cell remains 0 ( c_n+1(j) == 0 )

"""

"""
user input:
-number of cells (N)
-number of iterations (number of time steps)
-car density, fraction of cells that have cars on them, placed randomly
"""
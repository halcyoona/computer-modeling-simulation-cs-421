# RandomWalkAvg.py
#
# Introduction to Computational Science:  Modeling and Simulation for the Sciences, 2nd ed.
# Angela B. Shiflet and George W. Shiflet
# Wofford College
# Copyright 2014 by Princeton University Press
#

from math import sqrt
from random import randrange

# Function to return the average distance between first and last points of 100
# random walks, where steps are made on the diagonal
# Pre:  n is the number of steps.
# Post: The function returns the mean distance traveled.
def RandomWalkAvg(n):
    # determine points of path
    numTests = 100  # number of runs
    x0 = 0
    y0 = 0
    n = 25  # number of steps
    sumDist = 0   # sum of distances
    for j in range(numTests):
        x = x0
        y = y0
        for i in range(n):
            if randrange(2) == 0:
                x = x + 1
            else:
                x = x - 1
                
            if randrange(2) == 0:
                y = y + 1
            else:
                y = y - 1
        sumDist = sumDist + sqrt((x - x0)**2 + (y - y0)**2)

    return sumDist/numTests

    

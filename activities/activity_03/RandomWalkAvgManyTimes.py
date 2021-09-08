# RandomWalkAvgManyTimes.py
#
# Introduction to Computational Science:  Modeling and Simulation for the Sciences, 2nd ed.
# Angela B. Shiflet and George W. Shiflet
# Wofford College
# Copyright 2014 by Princeton University Press
#

from math import sqrt
from random import randrange

# Function to return list of average distances traveled in 100 random walks of n steps, 
# where n varies from 1 to 50
# Post: The function has returned a list of 50 average random-walk distances.
def RandomWalkAvgManyTimes():
    # determine points of path
    numTests = 100  # number of runs
    x0 = 0
    y0 = 0
    listDist = []  # list of distances
    for n in range(1, 51):
        sumDist = 0    # sum of distances
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

        listDist.append(sumDist/numTests)

    return listDist
    

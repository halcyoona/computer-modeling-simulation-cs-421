# RandomWalk.py
# Random walk simulation

# Introduction to Computational Science:  Modeling and Simulation for the Sciences, 2nd ed.
# Angela B. Shiflet and George W. Shiflet
# Wofford College
# Copyright 2014 by Princeton University Press

from random import *

# Random walk where steps are diagonal
# Pre:  n is the number of steps.
# Post: The function returns a list of 2 lists: a list of x-coordinates and a list
#       of y-coordinates taken in the random walk.
def RandomWalk(n):

    # determine points of path
    x = x0 = 0
    y = y0 = 0
    xLst = [0] 
    yLst = [0] 
    lst = [[0, 0]]
    for i in range(n):
        if randrange(2) == 0:
            x = x + 1
        else:
            x = x - 1
            
        if randrange(2) == 0:
            y = y + 1
        else:
            y = y - 1

        xLst.append(x)
        yLst.append(y)
        lst.append([x, y])
        
    return [xLst, yLst]


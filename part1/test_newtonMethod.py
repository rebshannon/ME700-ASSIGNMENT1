# Rebecca Shannon
# 2/4/2025
# tests for Newton's Method code, ME700 assignment 1 part 1

import numpy as numpy
import src.newtonMethod as newt
 

def test_calc_resid():
    known = np.array([5,18])
    found = newt.calc_resid([1,2])
    assert known == found

def test_calc_jacobian():
    known = 64
    found = newt.calc_jacobian(4)
    assert known == found

def test_maxIterReached():
    known = "Exiting"
    found = newt.maxIterReached(10,10)
    assert known == found

def test_nIterMaxCheck():
    known = "PASS: nIterMax is positive whole number"
    found = newt.nIterMaxCheck(10)
    knownf = "Exiting"
    foundf = newt.nIterMaxCheck(-1)
    assert known == found
    assert knownf == foundf
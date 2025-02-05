# Rebecca Shannon
# 2/4/2025
# tests for Newton's Method code, ME700 assignment 1 part 1

import numpy as np
import src.newtonMethod as newt
 

def test_calc_resid():

    def fnR(x):
        R[0] = x[0]**2 - 1 + x[1]
        R[1] = x[1]**3 - 1
        return fnR

    
    known = np.array([6],[26])
    found = newt.calc_resid(np.array([[2],[3]]),fnR)
    assert (known==found).all()

def test_calc_jacobian():
    def fnJ(x):
        J[0,0] = 2*x[0]
        J[0,1] = 0
        J[1,0] = 1
        J[1,1] = 3*x[1]**2
        return fnJ

    known = np.array([4,0],[1,27])
    found = newt.calc_jacob(np.array([[2],[3]]),fnJ)
    assert (known==found).all()

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
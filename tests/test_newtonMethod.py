# Rebecca Shannon
# 2/4/2025
# tests for Newton's Method code, ME700 assignment 1 part 1

import numpy as np
import src.newtonMethod as newt
 

def test_calc_resid():

    def fnR0(x,y,z=0):
        fnR0 = x**2 - 1 + y
        return fnR0

    def fnR1(x,y,z=0):
        fnR1 = y**3 -1
        return fnR1

    fnR = [fnR0,fnR1]
    
    known = np.array([[6, 26]])
    found = newt.calc_resid(np.array([[2],[3],[0]]),fnR)
    assert (known==found).all()
    
# def test_calc_jacob():

#     def fnJ00(x,y,z=0):
#         fnJ00 = 2*x
#         return fnJ00

#     def fnJ10(x,y,z=0):
#         fnJ10 = 0
#         return fnJ10

#     def fnJ01(x,y,z=0):
#         fnJ = 1
#         return fnJ10

#     def fnJ11(x,y,z=0):
#         fnJ2 = 3*y**2
#         return fnJ11

#     fnJ0 = [fnJ00,fnJ01]
#     fnJ1 = [fnJ10, fnJ11]
    
#     known = np.array([[4, 0],[1,27]])
#     found = newt.calc_jacob(np.array([[2],[3],[0]]),fnJ)
#     assert (known==found).all()


# def test_calc_jacobian():
#     def fnJ(x):
#         J[0,0] = 2*x[0]
#         J[0,1] = 0
#         J[1,0] = 1
#         J[1,1] = 3*x[1]**2
#         return fnJ

#     known = np.array([4,0],[1,27])
#     found = newt.calc_jacob(np.array([[2],[3]]),fnJ)
#     assert (known==found).all()

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
# Rebecca Shannon
# 2/4/2025
# Newton's Method code, ME700 assignment 1 part 1

import numpy as np
import scipy as sp

# USER INPUTS

x = 100
tol = 1e-9
maxIter = 1
nIter = 0
# function residual
# function Jacobian

# FUNCTIONS

def calc_resid(x:float) -> float:
    val = x**3 + 2*x**2 + 2
    return val

def calc_jacobian(x:float) -> float:
    val = 3*x**2 +4*x
    return val

def maxIterReached(maxIter: float, nIter: float):
    """Check if the naximum number of iterations has been reached and exit"""
    if nIter == maxIter:
        print("ERROR: Max number of iteractions exceeded.")
        #print("Last value found: C = ",C)
        print("Increase nIterMax or decrease tol")
        return "Exiting"
        exit()

def nIterMaxCheck(nIterMax: float):
    """Check if nIterMax is a postivie whole number, exits is false"""
    if nIterMax <= 0 or nIterMax.is_integer()==False:
        print("FAIL: maximum number of iterations must be a postivie whole number.")
        print("Change nIterMax to try again.")
        return "Exiting"
        exit()
    else: return "PASS: nIterMax is positive whole number"

# CHECK INPUTS
nIterMaxCheck(maxIter)

# FIRST LOOP
# calc R(x0) and J(0)
R = calc_resid(x)
J = calc_jacobian(x)

# calc inverse of Jacobian
dJ = 1/J
print(dJ)

# ACTUAL LOOP

while np.abs(R) > tol:
    x = x - dJ*R 

    # calc R(x0) and J(0)
    R = calc_resid(x)
    J = calc_jacobian(x)

    # calc inverse of Jacobian
    dJ = 1/J

    nIter =+ 1
    maxIterReached(maxIter,nIter)

print(x)
print(R)



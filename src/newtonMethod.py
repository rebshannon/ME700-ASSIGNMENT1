# Rebecca Shannon
# 2/4/2025
# Newton's Method code, ME700 assignment 1 part 1

import numpy as np
import scipy as sp

# USER INPUTS

x = np.array([1,2])
tol = 1e-9
maxIter = 1
nIter = 0


# FUNCTIONS

def calc_resid(x, fnR:callable):
    # check input size
    nRows = np.size(fnR)
    nCols = 1

    # initialize R
    R = np.zeros(nRows)
    np.matrix(R.reshape(nRows,1))

    if np.size(x) == 1:
        x[1] = 0
    elif np.size(x) == 2:
        x[1] = 0
        x[2] = 0

    iter = 0
    for func in fnR:
        R[iter] = func(x[0],x[1],x[2])
        iter =+ 1
    
    # return value
    np.matrix(R.reshape(nRows,nCols))
    return R

def calc_jacob(x,fnJ0: callable, fnJ1: callable, fnJ2: callable):
    # check input size
    nRows = np.size(fnJ,0)
    nCols = np.size(fnJ,1)

    # initialize R
    J = np.zeros(nRows*nCols)
    np.matrix(J.reshape(nRows,nCols))

    if np.size(x) == 1:
        x[1] = 0
    elif np.size(x) == 2:
        x[1] = 0
        x[2] = 0

    iter = 0
    rowJ = np.zeros(nCols)
    for rows in range(nRows):
         for cols in range(nCols):
             rowJ[cols] = fnJ[rows][cols](x[0],x[1],x[2])
             iter =+ 1

    # iter = 0
    # for func in fnJ:
    #     J[iter] = func(x[0],x[1],x[2])
    #     iter =+ 1
    
    # return value
    np.matrix(J.reshape(nRows,nCols))
    return J


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


    # SIZE R = SIZE X

# CHECK INPUTS
# nIterMaxCheck(maxIter)

# # FIRST LOOP
# # calc R(x0) and J(x0)
# R = calc_resid(x)
# J = calc_jacobian(x)

# # calc inverse of Jacobian
# dJ = np.linalg.inv(J)

# # ACTUAL LOOP

# while (R>tol).any():
#     x = x - dJ@R

#     # calc R(xi) and J(xi)
#     R = calc_resid(x)
#     J = calc_jacobian(x)

#     # calc inverse of Jacobian
#     dJ = np.linalg.inv(J)

#     # increment
#     nIter =+ 1
#     maxIterReached(maxIter,nIter)

# print(x)
# print(R)



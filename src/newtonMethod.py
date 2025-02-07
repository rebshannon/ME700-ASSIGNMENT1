# Rebecca Shannon
# 2/4/2025
# Newton's Method code, ME700 assignment 1 part 1

import numpy as np
import scipy as sp

def calc_resid(x, fnR:callable):
    # check input size
    nRows = np.size(fnR)
    nCols = 1

    # initialize R
    R = np.zeros(nRows)
    R = np.array(R.reshape(nRows,1))

    width = 3 - np.size(x)
    x = np.pad(x,[(0,width),(0,0)],'constant',constant_values=0)

    iter = 0
    for func in fnR:
        R[iter] = func(x[0],x[1],x[2])
        iter += 1
    
    # return value
    R = np.array(R.reshape(nRows,nCols))
    return R

def calc_jacob(x, fnJ: callable):
    # check input size
    nRows = np.size(fnJ,0)
    nCols = np.size(fnJ,1)

    # # initialize R
    J = np.zeros(nRows*nCols)
    J = np.array(J.reshape(nRows,nCols))

    # pad x array
    width = 3 - np.size(x)
    x = np.pad(x,[(0,width),(0,0)],'constant',constant_values=0)

    iter = 0
    rowJ = np.zeros(nCols)
    for rows in range(nRows):
          for cols in range(nCols):
                J[rows,cols] = fnJ[rows][cols](x[0],x[1],x[2])
                #   testFn = fnJ[rows][cols]
                #Jind = fnJ[rows][cols](x[0],x[1],x[2])
                #print(Jind)
                #J.item(iter) = Jind
            #   J[rows,cols] = Jind
                iter = iter + 1
    
    # return value
    J = np.array(J.reshape(nRows,nCols))
    return J

def maxIterReached(maxIter: float, nIter: float, x: float):
    """Check if the naximum number of iterations has been reached and exit"""
    if nIter == maxIter:
        print("ERROR: Max number of iteractions exceeded.")
        print("Last value found: x = ",x)
        print("Increase nIterMax or decrease tol")
        #return "Exiting"
        exit()
    return x

def nIterMaxCheck(nIterMax: float):
    """Check if nIterMax is a postivie whole number, exits is false"""
    if nIterMax <= 0 or nIterMax.is_integer()==False:
        print("FAIL: maximum number of iterations must be a postivie whole number.")
        print("Change nIterMax to try again.")
        #return "Exiting"
        exit()
    else: return "PASS: nIterMax is positive whole number"


    # SIZE R = SIZE X

def newtonMethodFunc(x, fnR: callable, fnJ: callable, tol=1e-9, maxIter=1000):

    # FIRST LOOP
    # find initial R(x0) and J(x0)
    # check for matrix or algebra
    if np.size(fnR) > 1:
        R = calc_resid(x,fnR)
        J = calc_jacob(x, fnJ)
        invJ = np.linalg.inv(J)
    else:
        R = fnR(x)
        J = fnJ(x)
        invJ = 1/J
        print(R)
        
    # # ACTUAL LOOP

    while (np.abs(R)>tol).any():

        if np.size(fnR) > 1:
            x = x - invJ @ R
            R = calc_resid(x,fnR)
            J = calc_jacob(x, fnJ)
            invJ = np.linalg.inv(J)
        else:
            x = x - invJ * R
            R = fnR(x)
            J = fnJ(x)
            invJ = 1/J
        print(R)
        print(x)
    print("FINAL")
    print(R)
    print(x)
    return x,R

    
    

# # increment
# nIter += 1
# print(nIter)
# maxIterReached(maxIter,nIter,x)

# print(x)
# print(R)
# print(J)
# print(invJ)



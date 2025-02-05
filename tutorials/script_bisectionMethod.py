# REBECCA SHANNON
# 1/25/2025
# Bisectional method code, assignment 1 warm up ME 700

import numpy as np
import src.bisectionMethodFns as fnA1 
import exampleSolutions as exSoln



"""
****** USER INPUTS ***** 
"""

A = 0         # initial guess #1
B = 60           # initial guess #2
nIterMax = 50   # max number of iterations
tol = 1e-9      # desired tolerance

"""
****** CHECK INPUTS ***** 
"""

#check: is nIterMax a postitive whole number
fnA1.nIterMaxCheck(nIterMax)

# check: is A < B
print(fnA1.A_lessThan_B(A,B))

# calc f(A) and f(B) 
fA = exSoln.exFn(A)
fB = exSoln.exFn(B)

# check: do f(A) and f(B) have opposite signs?
fnA1.A_B_signCheck(fA,fB)

"""
***** BISECTION METHOD *****
"""

for nIter in range(1, nIterMax+1):
    
    # find midpoint
    C = fnA1.midpoint_A_B(A, B)
    fC = exSoln.exFn(C)

    # if within tolerance, read final answer and exit
    fnA1.checkTol(fC,tol, C, nIter)

    # if not within tolerance, reassign C and start again
    A,B = fnA1.reassignC(fA,fB,fC,A,B,C)

    # exit if this is the last loop
    fnA1.maxIterReached(nIterMax, nIter, C)

    # increment iteration counter
    nIter += 1

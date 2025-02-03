# Functions needed for bisectionMethod.py
# ME 700 Assignment 1
# Rebecca Shannon 1/25/25

import numpy as np
import exampleSolutions as exSoln

def A_lessThan_B(A: float, B: float):
    """Given A and B, check if A < B"""
    if A > B or A == B: 
        return "FAIL: A should be less than B, exiting"
        exit()
    else: return "PASS: A is less than B"

def nIterMaxCheck(nIterMax: float):
    """Check if nIterMax is a postivie whole number, exits is false"""
    if nIterMax <= 0 or nIterMax.is_integer()==False:
        print("FAIL: maximum number of iterations must be a postivie whole number.")
        print("Change nIterMax to try again.")
        return "Exiting"
        exit()
    else: return "PASS: nIterMax is positive whole number"

def A_B_signCheck(fA: float, fB: float):
    """Checks if f(A) and f(B) have opposite signs"""
    if np.sign(fA) == np.sign(fB):
        print("FAIL: f(A) and f(B) should have opposite signs:")
        print("f(A) = ",fA)
        print("f(B) = ",fB)
        print("Change inputs A and B")
        return "Exiting"
        exit()
    else: return "PASS: f(A) and f(B) have opposite signs"


def midpoint_A_B(A: float, B: float) -> float:
    """Given two float values, find the midpoint between them."""
    val = (A + B)/2
    return val

def checkTol(fC: float, tol: float, C: float, nIter: float):
    """Check if f(C) is within the given tolerance"""
    if np.abs(fC) < tol:
        print("Root found in ", nIter, " iterations")
        print("C =", C)
        print("f(C) = ", fC)
        exit()
        return "Solution found"
          

def reassignC(fA: float, fB: float, fC: float, A: float, B: float,C: float) -> float:
    """Reassign C to A or B based on the sign of f(C)"""
    if np.sign(fC) == np.sign(fA): 
        valA = C
        valB = B
    else: 
        valA = A
        valB = C
    return valA, valB

def maxIterReached(nIterMax: float, nIter: float, C: float):
    """Check if the naximum number of iterations has been reached and exit"""
    if nIter == nIterMax:
        print("ERROR: Max number of iteractions exceeded.")
        print("Last value found: C = ",C)
        print("Increase nIterMax or decrease tol")
        return "Exiting"

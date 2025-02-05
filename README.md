# ME700 Assignment 1
## Table of Contents
* [Bisection Method](#bim)
* [Newton's Method](#newt)

## Warm Up: Bisection Method <a name="bim"></a>

### About the Solver

Uses the bisection method to find the root $(x = C)$ of a provided function $f(x)$ based on the user's initial guesses $(x = A,~B)$. The tolerance and maximum number of iterations are also defined by the user. The `numpy` library is needed to run this solver. See *tutorials/tutSoln_bisectionMethod* for instructions on using the solver and example problems.

### Definitions

__Variables__  
`A`: initial guess, lower bound  
`B`: initial guess, upper bound  
`C`: midpoint of $A$ and $B$; solution  
`nIterMax`: maximum number of iterations for the solver  
`tol`: desired tolerance level

__Files__  
Unless otherwise noted, all are **.py* files  
*tutorials/script_bisectionMethod*: user inputs defined here; solver is run from this script  
*tutorials/tutSoln_bisectionMethod*: defines the fuction that will be solved with *script_bisectionMethod.py* 
*tutorials/tutorial_bisectionMethod.md*: instructions for how to use the bisection method solver and examples
*src/bisectionMethodFns*: Python functions associated with *script_bisectionMethod.py*  
*tests/test_bisectionMethod.py*: tests for *bisectionMethodFns.py* functions  
 
## Part 1: Newton's Method <a name="newt"></a>
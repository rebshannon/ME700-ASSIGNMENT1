# ME700 Assignment 1
## Table of Contents
* [Set Up] (#setup)
* [Bisection Method](#bim)
* [Newton's Method](#newt)

## Set Up <a name=setup></a>
Set up the conda environment and test that the code is functioning.  

1. Create a new conda environment and activate it.  
    ```bash 
    conda create --name A1-bisection-method-env python=3.12
    ```
    ```bash
    conda activate A1-bisection-method-env
    ``` 
2. Confirm that the right version of Python and pip setuptools are being used. Python should be version 3.12; the second command will update setuptools if necessary.  
    ```bash
    python --version
    ```
    ```bash
    pip install --upgrade pip setuptools wheel
    ```
3. Navigate to the warmUp directory.  
4. Install an editable version of the code. Note that the *pyproject.toml* file is required for this.  
    ```bash
    pip install -e .
    ```
5. Test the code with pytest. This command returns code coverage for all files in the directory. Coverage for *src/bisectionMethodFns.py* should be 100% and all tests should pass.  
    ```bash
    pytest -v --cov=src  --cov-report term-missing
    ```

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

### About the solver

Uses the Newton-Rhapsom method to find the root of a provided function(s) based on the user's initial guesses. The tolerance and maximum number of iterations are also defined by the user. The `numpy` library is needed to run this solver. 

### Variables

`x`: initial guess, vector must be the same size as `R`  
`fnR`: function(s) to be solved, each row is a different function, number of variables must equal number of functions  
`fnJ`: Jacobian matrix, deriva, must be a square matrix with dimention equal to the number of rows in `fnR`  
`nIterMax`: maximum number of iterations for the solver  
`tol`: desired tolerance level  

### Files

*src/newtonMethod.py*: holds Newton method function along with other functions necessary for solving
*tests/test_newtonMethod.py*: tests for *newtonMethod.py*
*tutorials/tut_newtonMethod.ipynb*: Jupyter notebook with example problems and solutions

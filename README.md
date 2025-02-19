# ME700 Assignment 1

[![python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
![os](https://img.shields.io/badge/os-ubuntu%20|%20macos%20|%20windows-blue.svg)
[![license](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/sandialabs/sibl#license)

[![codecov](https://codecov.io/gh/rebshannon/ME700-ASSIGNMENT1/graph/badge.svg?token=S3ZCVIAW6K)](https://codecov.io/gh/rebshannon/ME700-ASSIGNMENT1)
[![tests](https://github.com/rebshannon/ME700-ASSIGNMENT1/actions/workflows/test.yml/badge.svg)](https://github.com/rebshannon/ME700-ASSIGNMENT1/actions)



## Table of Contents

* [Set Up](#setup)
* [Bisection Method](#bim)
* [Newton's Method](#newt)
* [Elasto-Plastic Materials](#elast)

## Set Up <a name=setup></a>
Set up the conda environment and test that the code is functioning. Note: The environemnt name for all parts of Assignemnt 1 refers to the bisection method.  

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
3. Make sure you are in the ME700-Assignment1 directory.  
4. Install an editable version of the code. Note that the *pyproject.toml* file is required for this.  
    ```bash
    pip install -e .
    ```
5. Test the code with pytest. This command returns code coverage for all files in the directory. Coverage for each of the solvers should be 100% and all tests should pass.  
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
* *tutorials/script_bisectionMethod*: user inputs defined here; solver is run from this script  
* *tutorials/tutSoln_bisectionMethod*: defines the fuction that will be solved with *script_bisectionMethod.py* 
* *tutorials/tutorial_bisectionMethod.md*: instructions for how to use the bisection method solver and examples
* *src/bisectionMethodFns*: Python functions associated with *script_bisectionMethod.py*  
* *tests/test_bisectionMethod.py*: tests for *bisectionMethodFns.py* functions  
 
## Part 1: Newton's Method <a name="newt"></a>

### About the solver

Uses the Newton-Rhapsom method to find the root of a provided function(s) based on the user's initial guesses. The tolerance and maximum number of iterations are also defined by the user. The `numpy` library is needed to run this solver. 

### Variables

`x`: initial guess, 1D array must be the same size as `R`  
`fnR`: 1D array, function(s) to be solved, each row is a different function, number of variables must equal number of functions  
`fnJ`: Jacobian matrix (derivatives), must be a square matrix with dimension equal to the number of rows in `fnR`  
`nIterMax`: maximum number of iterations for the solver  
`tol`: desired tolerance level  

### Files

* *src/newtonMethod.py*: holds Newton method function along with other functions necessary for solving
* *tests/test_newtonMethod.py*: tests for *newtonMethod.py*
* *tutorials/tut_newtonMethod.ipynb*: Jupyter notebook with example problems and solutions

### Running the Code

The following steps can be completed to launch a Jupyter notebook containing the example problems.

```bash
pip install jupyter
```
```bash
cd tutorials/
```
```bash
jupyter notebook tut_newtonMethod.ipynb
```

## Part 2: Elsasto-Plastic Materials <a name="elasto"></a>

### About the solver

This solver takes user provided strain curve and material properties and finds the material stress at each point on the strain curve. It accounts for both elastic and plastic deformation. The material can eitehr undergo isotropic hardening or kinmatic hardening. In isotropic hardening, the yield surface expands uniformly in all directions when experiencing plastic deformation. In kinematic hardening, plastic deformation causes the the yield surface to change poisition without changing size.

### Classes

`ElastoPlastic`  
* Parent class for both isotropic hardening and elastoplastic hardening  
* User defined attributes:  
    * `E` :  Young's modulus
    * `H` : Plastic modulus
    * `Y_o` : initial yield stress
* Default attributes:
    * `sigma_n` : material stress at load step _n_
    *  `epsilon_p_n` : plastic strain at load step _n_

`IsotropicHardening`
* Child class for isotropic hardening
* Attributes: same as ElastoPlastc class

`kinematicHardening`
* Child class for kinematic hardening
* Attributes: same as ElastoPlastc class
* Additional default attribute: 
    * `alpha_n` : back stress at load step _n_


### Files

* *src/elastoPlasticClasses.py*: holds the ElastoPlastic classes and functions to solve for material stresses
* *tests/test_elastPlastic.py*: tests for *elastoPlasticClasses.py*
* *tutorials/tut_ElastPlastic.ipynb*: Jupyter notebook with example problems and solutions

### Running the Code

To use the solver, the Young's modulus $E$, plastic modulus $H$, and initial yield stress $Y_o$ of the material must be known. If the plastic modulus is not known, it can be found from Young's moudlus and the tangent modulus $E_t$.

$$H = \frac{EE_t}{E-E_T}$$   

In addition to the material properties, the applied strain should be provided in discreet load steps. The user also needs to specify whether the material is experiencing isotropic or kinematic hardening. The following steps can be completed to launch a Jupyter notebook containing the example problems.

```bash
pip install jupyter
```
```bash
cd tutorials/
```
```bash
jupyter notebook tut_elastPlastic.ipynb
```

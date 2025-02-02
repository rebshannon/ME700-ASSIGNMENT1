
# ME700 Assignment 1 Warm Up

Rebecca Shannon  
2/3/2025  

## About the Solver

Uses the bisection method to find the root $(x = C)$ of a provided function $f(x)$ based on the user's initial guesses $(x = A,~B)$. The tolerance and maximum number of iterations are also defined by the user. The `numpy` library is needed to run this solver.

## Definitions

__Variables__  
`A`: initial guess, lower bound  
`B`: initial guess, upper bound  
`C`: midpoint of $A$ and $B$; solution  
`nIterMax`: maximum number of iterations for the solver  
`tol`: desired tolerance level

__Files__  
All are **.py* files  
*bisectionMethod*: user inputs defined here; solver is run from this script  
*fnAssignment1*: Python functions associated with *bisectionMethod.py*  
*exampleSolutions*: defines the fuction that will be solved with *bisectionMethod.py*  
*test_pytest.py*: tests for *fnAssignment1.py* functions

## Using the code

### Initial Setup
Set up the conda environment and test that the code is functioning.  
1. Create a new conda environment and activate it.  
```bash 
conda create --name A1-bisection-method-env python=3.12
conda activate A1-bisection-method-env
``` 
2. Confirm that the right version of Python and pip setuptools are being used. Python should be version 3.12; the second command will update setuptools if necessary.  
```bash
python --version
pip install --upgrade pip setuptools wheel
```
3. Navigate to the warmUp directory.  
4. Install an editable version of the code. Note that the *pyproject.toml* file is required for this.  
```bash
pip install -e .
```
5. Test the code with pytest. This command returns code coverage for all files in the directory. Coverage for *warmUp/fnAssignment1.py* should be 100% and all tests should pass.  
```bash
pytest -v --cov=warmUp  --cov-report term-missing
```
### Running Examples
Instructions on how to run the example cases. Two files should be modified: *exampleSolutions.py* and *bisectionMethod.py*. 

In *exampleSolutions.py*, there are five functions defined, all of which are called `exfn`, so only one can be uncommented at a time. Select the example that you would like to complete and uncomment it (from the line starting with `def` to the line starting with `return`). Make sure all other functions are comments.


In *bisectionMethod.py*, four user inputs are required: two initial guesses (`A` and `B`), the maximum number of iterations (`nIterMax`), and the desired tolerance level (`tol`). Three conditions must be met for the user inputs:

1. `A` < `B`
2. `sign[f(A)]` $\neq$ `sign[f(B)]`
3. `nIterMax` must be a positive whole number

Enter these four values in the **USER INPUTS** section. Run the *bisectionMethod.py* Python file to run the example. Results will be printed to the terminal.

### Running New Cases

This script can also use used for other user defined functions. This can be done by adding functions to the *exampleSolutions.py* file. Each function should be called `exFn` to be compatible with the *bisectionmethod* script. Additionally, the function should only take one input and return one value.


## Examples

### Example 1: Polynomial \#1

Use the bisection method to find the root of the following equation:  
$$y = x^3 + 3x - 1$$

### Example 2: Polynomial \#2

To use the bisection method, the governing equations needs to be of the form $f(x) = 0$ in order to find the roots. This means that some equations need to be rearranged to be used with this method. Use the bisection method to find when $y = 5$ in the following equation:

$$y = -\frac{1}{2}x^3 + 2x^2 - 4$$

### Example 3: Spring Energy

The potential energy stored in a spring is defined as

$$U_s=\frac{1}{2}k x^2$$

where $U_s$, $k$, and $x$ are the spring potential energy, spring constant, and spring displacement, respectively. Consider a spring whose equilibrium length is $x = 10cm$ that has a spring constant of $k = 10N/m$. At what length does the spring have an potential enerrgy of $U_s=0.033J$?

### Example 4: Bernoulli's Equation

When considering incompressible, steady flow with no friction, Bernoulli's Equation can be used to describe the total pressure at any point along a streamline. Assuming a constant height (i.e. constant gavity effects), Bernoulli's priciple is written as

$$p_1+\frac{1}{2}\rho v_1^2 = p_2+\frac{1}{2}\rho v_2^2$$

Where $p$, $\rho$, and $v$ are the static pressure, fluid density, and fluid velocity. The subscripts $\{1,2\}$ indicate the two different locations along the streamline. At point $1$, water $(\rho = 997 kg/m^3)$ is travelling in a pipe with a static pressure of $1\times10^5Pa$ and a velocity of $10m/s$. At point $2$, the area of the pipe has decreased, so the pressure has decreased to $5\times10^4 Pa$. What is the fluid velocity at point $2$?

### Example 5: Kinematic Equation

The motion of an opject travelling with a specified initial velocity and constant acceleration can be described by the following equation.
$$\Delta x = v_i t+\frac{1}{2}at^2$$

where $\Delta x$, $v_i$, $t$, and $a$ are the distance travelled, initial velocity, time, and acceleration, respectively. If a car starts from rest and moves with a constant acceleration of $3 m/s^2$, how long does it take the car to travel $1000 m$?

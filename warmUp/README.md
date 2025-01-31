
# ME700 Assignment 1

Rebecca Shannon  
1/29/2025  
Python 3.12.8

## About the Solver

Uses the bisection method to find the root $(x = C)$ of a provided function $f(x)$ based on the user's initial guesses $(x = A,~B)$. The tolerance and maximum number of iterations are also defined by the user. The `numpy` library is needed to run this solver.

## Definitions

$A$: initial guess, lower bound  
$B$: initial guess, upper bound  
$C$: midpoint of $A$ and $B$; solution  
$nIterMax$: maximum number of iterations for the solver  
$tol$: desired tolerance level

*bisectionMethod*: user inputs defined here; solver is run from this script  
*fnAssignment1*: Python functions associated with *bisectionMethod*  
*exampleSolutions*: defines the fuction that will be solved with *bisectionMethod*  
*test_pytest.py*: tests for *fnAssignment1* functions (Only functions that return values are tested. Functions that test/verify values return a PASS/FAIL output when *bisectionMethod* is run.)

## Using the code

In the *bisectionMethod.py* script, four user inputs are required: two initial guesses $(A$ and $B)$, the maximum number of iterations $(nIterMax)$, and the desired tolerance level $(tol)$. Three conditions must be met for the user inputs:

1. $A < B$
2. $sign[f(A)] \neq sign[f(B)]$
3. $nIterMax$ must be a positive whole number

The function $f(x)$ that is being solved should be defined in a separate Python script and imported as *exSoln*. The solutions to these examples are currently held in *exampleSolutions.py*. All constants needed for the desired function should also be defined here. In this script,  uncomment the function associated with the example problem that you are atttempting. When moving on to another example, make sure to comment out the old example function (e.g. only one function in *exampleSolutions.py* should be uncommented at a time).

To test the functions, run the `pytest <workdir>` command in the terminal. Note `\<workDir\>` indicates the directory in which the assignment is stored.

First, set up the environment and activate it. 

```bash
conda create --name A1-bisectionMethod-env python=3.12
conda activate A1-bisectionMethod-env
```

Confirm that the right version of python is installed (3.12) and that the most up to date version of setuptools is being used in pip.
```bash
python --version
pip install --upgrade pip setuptools wheel
```
"Create an editable install of the bisection method code (you must be in the correct directory)."
```\bash
pip install -e .
```

Run pytest to test the code. T


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

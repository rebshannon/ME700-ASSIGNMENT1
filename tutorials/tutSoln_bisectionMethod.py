# REBECCA SHANNON
# 1/25/2025
# Bisectional method code, assignment 1 warm up ME 700

# EXAMPLE SOLUTIONS
# Uncomment the code for the desired example

# EXAMPLE 1: Polynomial 1
def exFn(x: float) -> float:

    """ Polynomial example for bisection method """
    val = x**3 - 2*x**2 + 3*x - 1 
    return val

# EXAMPLE 2: Polynomial 2
# def exFn(x: float) -> float:
#     """ Second polynomial example """

#     val = -0.5*x**3 + 2*x**2 - 4 - 5
#     return val


# EXAMPLE 3: Spring Energy
# def exFn(x: float) -> float:
#     """ Bisection method for finding spring length from energy stored """
     
#     # define constants
#     k = 10
#     x0 = 0.1
#     Us = 0.033

#     val = 1/2 * k * (x0**2 - x**2) - Us
#     return val

# EXAMPLE 4: Bernoulli
# def exFn(v2: float) -> float:
#     """ Using the bisection method with Bernoulli's Equation"""
#     # define constants
#     p1 = 1e5
#     rho = 997
#     v1 = 10
#     p2 = 5e4

#     # bernouli equation
#     val = p1 + 1/2*rho*v1**2 - p2 - 1/2*rho*v2**2
#     return val


# # EXAMPLE 5: Kinematics
# def exFn(t: float) -> float:
#     """ Bisection method for kinematic equation """
     
#     # define constants
#     vi = 0
#     a = 3
#     x = 1000

#     val = vi*t + 1/2*a*t**2 - 1000
#     return val
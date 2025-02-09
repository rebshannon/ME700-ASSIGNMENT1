import numpy as np
import newtonMethod as newt

#old loop
    # tol = 1e-9
    # x = np.array([2])
    # R=np.zeros((1,1))
    # J = np.zeros((1,1))

    # R[0] = x[0]**2 - 2
    # #2*x[0]**2 + 2*x[1] + 2*x[0]
    # #R[1] = -x[0]**3 - 7*x[1] -7

    # J[0] = 2*x[0]

    # # J[0,0] = 4*x[0] + 2*x[1] +2
    # # J[0,1] = -3*x[0]**2 - 7*x[1]
    # # J[1,0] = 2*x[0]**2 + 2 +2*x[0]
    # # J[1,1] = -x[0]**3 - 7

    # dJ = np.linalg.inv(J)

    # while (R>tol).any():
        
    #     x = x - dJ@R
    #     print(x)

    #     R[0] = x[0]**2 - 2
    #     J[0] = 2*x[0]

    #     # R[0] = 2*x[0]**2 + 2*x[1] + 2*x[0]
    #     # R[1] = -x[0]**3 - 7*x[1] -7

    #     # J[0,0] = 4*x[0] + 2*x[1] +2
    #     # J[0,1] = -3*x[0]**2 - 7*x[1]
    #     # J[1,0] = 2*x[0]**2 + 2 +2*x[0]
    #     # J[1,1] = -x[0]**3 - 7
        
    #     dJ = np.linalg.inv(J)

    # #     nIter =+ 1
    # #     maxIterReached(maxIter,nIter)

    # print(x)
    # print(R)



# USER INPUTS

x = np.array([2])
tol = 1e-9
maxIter = 1000

# FUNCTIONS HERE FOR TESTING

def fnR(x):
    fnR = x**3-2+x
    return fnR

def fnJ(x):
    fnJ = 3*x**2+1
    return fnJ

# CALL FUNCTION
C = newt.newtonMethodFunc(x,fnR,fnJ,tol,maxIter)
print(C)

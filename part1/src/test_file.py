import numpy as np

tol = 1e-9
x = np.array([[2],[1]])
R=np.zeros((2,1))
J = np.zeros((2,2))

R[0] = 2*x[0]**2 + 2*x[1] + 2*x[0]
R[1] = -x[0]**3 - 7*x[1] -7

J[0,0] = 4*x[0] + 2*x[1] +2
J[0,1] = -3*x[0]**2 - 7*x[1]
J[1,0] = 2*x[0]**2 + 2 +2*x[0]
J[1,1] = -x[0]**3 - 7

np.matrix(x.reshape(2,1))
np.matrix(R.reshape(2,1))
np.matrix(J.reshape(2,2))

print(R)
print(J)

dJ = np.linalg.inv(J)

print(dJ)

#while np.any(R) > tol:
    
x = x - dJ@R
print(x)

    # R[0] = 2*x[0]**2 + 2*x[1] + 2*x[0]
    # R[1] = -x[0]**3 - 7*x[1] -7

    # J[0,0] = 4*x[0] + 2*x[1] +2
    # J[0,1] = -3*x[0]**2 - 7*x[1]
    # J[1,0] = 2*x[0]**2 + 2 +2*x[0]
    # J[1,1] = -x[0]**3 - 7
    
    # dJ = np.linalg.inv(J)

#     nIter =+ 1
#     maxIterReached(maxIter,nIter)

# print(x)
# print(R)

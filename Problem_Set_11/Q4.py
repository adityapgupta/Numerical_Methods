import numpy as np
from Q2 import gauss_jacobi

A = np.array([[1,2,3],[2,-1,2],[3,1,-2]])
b = np.array([5,1,-1])

print(gauss_jacobi(A,b,[0,0,0]))
import numpy as np
from Q3 import gauss_seidel

A = np.array([[2,8,3,1],[0,2,-1,4],[7,-2,1,2],[-1,2,5,0]])
b = np.array([-2,4,3,5])

print(gauss_seidel(A,b,[0,0,0,0]))
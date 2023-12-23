import numpy as np
import math

def linear_difference(f,a,b,y_a,y_b,n):
    h = (b-a)/(n+1)
    x = np.linspace(a,b,n+2)

    A = np.zeros((n,n))
    b = np.zeros(n)

    b[0] += h**2*f(x[1])[2] - (1+h*f(x[1])[0]/2)*y_a
    b[n-1] += h**2*f(x[n])[2] - (1-h*f(x[n])[0]/2)*y_b
    for i in range(1,n-1):
        b[i] += h**2*f(x[i+1])[2]
    
    for i in range(n):
        A[i,i] += -(2 + h**2*f(x[i+1])[1])
        if i < n-1:
            A[i,i+1] += 1 - h*f(x[i+1])[0]/2
            A[i+1,i] += 1 + h*f(x[i+2])[0]/2
    
    return np.linalg.solve(A,b)
        

def f(x):
    return (-2/x, 2/x**2, math.sin(math.log(x))/x**2)

if __name__ == '__main__':
    print(linear_difference(f,1,2,1,2,9))
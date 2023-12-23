import math
import numpy as np

def newton_raphson(f, df, x0, tol=1e-5, maxiter=1000):
    x = x0
    for i in range(maxiter):
        fx = f(x)
        if abs(fx) < tol:
            return x, i
        x = x - fx/df(x)
        print(x, i)
    return "No solution found"

def f(x):
    if x >= 0:
        return np.cbrt(x**2)
    else:
        return -1*np.cbrt(x**2)

def df(x):
    if x >= 0:
        return (2/3)*np.cbrt(1/x)
    else:
        return -(2/3)*np.cbrt(1/x)

x, i = newton_raphson(f, df, 1)
print(x, i)

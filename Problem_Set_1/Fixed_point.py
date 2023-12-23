import math

def fixed_point(f, x0, tol=1e-4, maxiter=1000):
    x = x0
    for i in range(maxiter):
        fx = f(x)
        if abs(fx-x) < tol:
            return x, i
        x = fx
    return "No solution found"

def f(x):
    return x**2 - 2 - math.cos(x) + x

x, i = fixed_point(f, 0)
print(x, i)


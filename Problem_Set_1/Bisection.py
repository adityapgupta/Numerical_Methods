import math

def bisection(f,a,b,tol=1e-4,maxiter=100):
    fa = f(a)
    fb = f(b)

    if fa*fb > 0:
        return "No solution found"

    for i in range(maxiter):
        c = (a+b)/2.0
        print(c)
        fc = f(c)
        if fa*fc < 0:
            b = c
        else:
            a = c
            fa = fc
        if abs(b-a) < tol:
            return c, i
    return "No solution found"

def f(x):
    return x**3+x-2   

c, i = bisection(f, 0, 3)
print(c, i)
import math

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def f(x):
    return x**2+ math.cos(x)

print(midpoint(f,0,4))
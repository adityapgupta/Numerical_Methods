import math

def simpson(f, a, b):
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6

def f(x):
    return (math.cos(x))**2

p = simpson(f, 0, math.pi/3)

print(p)
print(math.pi/3 - p)
import math

def transform(x,a,b):
    return (b-a)/2*x + (b+a)/2

def two_point_gaussian(f,a,b):
    return (b-a)/2*(f(transform(-1/math.sqrt(3),a,b)) + f(transform(1/math.sqrt(3),a,b)))

def f(x):
    return x*math.sin(x)

print(two_point_gaussian(f,0,math.pi/2))
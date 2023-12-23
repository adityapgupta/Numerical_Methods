import math

def transform(x,a,b):
    return (b-a)/2*x + (b+a)/2

def one_point_gaussian(f,a,b,c,d):
    return (b-a)*(d-c)*f(transform(0,a,b),transform(0,c,d))

def two_point_gaussian(f,a,b,c,d):
    return (b-a)*(d-c)/4*(f(transform(-1/math.sqrt(3),a,b),transform(-1/math.sqrt(3),c,d)) + f(transform(1/math.sqrt(3),a,b),transform(1/math.sqrt(3),c,d))+f(transform(-1/math.sqrt(3),a,b),transform(1/math.sqrt(3),c,d))+f(transform(1/math.sqrt(3),a,b),transform(-1/math.sqrt(3),c,d)))

def f(x,y):
    return math.log(x+2*y)

print(one_point_gaussian(f,1.4,2.0,1.0,1.5))
print(two_point_gaussian(f,1.4,2.0,1.0,1.5))
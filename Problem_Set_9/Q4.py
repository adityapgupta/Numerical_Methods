import math
from Q3 import non_linear_shooting

def f_1(x,y):
    return y[1], -(y[1])**2 - y[0] + math.log(x)

def f_2(y,z):
    return z[1], -z[0] - 2*y[1]*z[1]

def f_0(x):
    return math.log(x)

non_linear_shooting(f_0,f_1,f_2,1,2,0,math.log(2),0.5,10,1e-5)
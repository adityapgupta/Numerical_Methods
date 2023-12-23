import math

from Q1 import taylor_2
from Q2 import rk_2, rk_2_mid
from Q3 import trapezoidal

def f(x,y):
    return (1 + y/x)

def f_1(f,x,y):
    return (-y/x**2 + f(x,y)/x)

def exact(x):
    return (x*math.log(x) + 2*x)

print(taylor_2(f,f_1,1,2,2,0.25), abs(taylor_2(f,f_1,1,2,2,0.25)-exact(2)))
print(rk_2(f,1,2,2,0.25), abs(rk_2(f,1,2,2,0.25)-exact(2)))
print(rk_2_mid(f,1,2,2,0.25), abs(rk_2_mid(f,1,2,2,0.25)-exact(2)))
print(trapezoidal(f,1,2,2,0.25), abs(trapezoidal(f,1,2,2,0.25)-exact(2)))

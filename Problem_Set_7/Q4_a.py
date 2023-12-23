import math

from Q1 import taylor_2
from Q2 import rk_2, rk_2_mid
from Q3 import trapezoidal

def f(x,y):
    return (x*math.exp(3*x)-2*y)

def f_1(f,x,y):
    return (math.exp(3*x) + x*3*math.exp(3*x) - 2*f(x,y))

def exact(x):
    return (x*math.exp(3*x)/5 - math.exp(3*x)/25 + math.exp(-2*x)/25)

print(taylor_2(f,f_1,0,1,0,0.5), abs(taylor_2(f,f_1,0,1,0,0.5)-exact(1)))
print(rk_2(f,0,1,0,0.5), abs(rk_2(f,0,1,0,0.5)-exact(1)))
print(rk_2_mid(f,0,1,0,0.5), abs(rk_2_mid(f,0,1,0,0.5)-exact(1)))
print(trapezoidal(f,0,1,0,0.5), abs(trapezoidal(f,0,1,0,0.5)-exact(1)))

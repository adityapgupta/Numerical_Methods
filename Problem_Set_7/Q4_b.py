import math

from Q1 import taylor_2
from Q2 import rk_2, rk_2_mid
from Q3 import trapezoidal

def f(x,y):
    return (1 + (x-y)**2)

def f_1(f,x,y):
    return (2*(x-y)*(1-f(x,y)))

def exact(x):
    return (x + 1/(1-x))

print(taylor_2(f,f_1,2,3,1,0.5), abs(taylor_2(f,f_1,2,3,1,0.5)-exact(3)))
print(rk_2(f,2,3,1,0.5), abs(rk_2(f,2,3,1,0.5)-exact(3)))
print(rk_2_mid(f,2,3,1,0.5), abs(rk_2_mid(f,2,3,1,0.5)-exact(3)))
print(trapezoidal(f,2,3,1,0.5), abs(trapezoidal(f,2,3,1,0.5)-exact(3)))

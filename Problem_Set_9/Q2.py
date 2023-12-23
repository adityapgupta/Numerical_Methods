import math
from Q1 import linear_shooting

def f_1(x,y):
    return y[1], 4*y[0] - 4*x

def f_2(x,y):
    return y[1], 4*y[0]

def f_0(x):
    return math.exp(2)*(math.exp(4) - 1)**(-1)*(math.exp(2*x) - math.exp(-2*x)) + x

linear_shooting(f_0,f_1,f_2,0,1,(0,0),(0,1),2,0.25)
import math
import numpy as np
from Q1 import linear_difference

def f(x):
    return (0, -4, math.cos(x))

def f_0(x):
    return -math.cos(2*x)/3 - math.sqrt(2)*math.sin(2*x)/6 + math.cos(x)/3

print(linear_difference(f,0,math.pi/4,0,0,4))

actual = [f_0(x) for x in np.linspace(0,math.pi/4,6)]
print(actual[1:-1])
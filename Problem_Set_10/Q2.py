import math
from Q1 import linear_difference

def f(x):
    return (-(x+1), 2, (1-x**2)*math.exp(-x))

print(linear_difference(f,0,1,1,0,9))
print(linear_difference(f,0,1,1,0,19))

import math

def diff_forward(f, f_2, a, h):
    derivative = (f(a+h) - f(a))/h
    error = abs(-f_2(a)*h/2)

    return derivative, error

def f(x):
    return math.log(x)

def f_2(x):
    return -1/x**2

print(diff_forward(f, f_2, 1.8, 0.1))
print(diff_forward(f, f_2, 1.8, 0.05))
print(diff_forward(f, f_2, 1.8, 0.01))

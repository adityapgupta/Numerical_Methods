import math

def diff_backward(f, f_2, a, h):
    derivative = (f(a-h) - f(a))/(-h)
    error = abs(f_2(a-h)*h/2)

    return derivative, error

def diff_central(f, f_3, a, h):
    derivative = (f(a+h) - f(a-h))/(2*h)
    error = abs(-f_3(a-h)*h**2/6)

    return derivative, error

def f(x):
    return math.log(x)

def f_2(x):
    return -1/x**2

def f_3(x):
    return 2/x**3

print(diff_backward(f, f_2, 1.8, 0.1))
print(diff_backward(f, f_2, 1.8, 0.05))
print(diff_backward(f, f_2, 1.8, 0.01))

print(diff_central(f, f_3, 1.8, 0.1))
print(diff_central(f, f_3, 1.8, 0.05))
print(diff_central(f, f_3, 1.8, 0.01))


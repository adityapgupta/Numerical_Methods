import math

def ivp_solver(f,a,b,y_a,h):
    y = y_a
    x = a
    while x <= b:
        y = y + h*f(x,y)
        x = x + h
    return y
    
def f(x,y):
    return 2*x*y**2

print(ivp_solver(f,0,1,0.5,0.1))
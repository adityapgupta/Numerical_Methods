import math

def ivp_solver(f,a,b,y_a,h):
    y = y_a
    x = a
    while x <= b:
        y = y + h*f(x,y)
        x = x + h
    return y
    
def f(x,y):
    return y*math.log(y)/x

print(ivp_solver(f,2,3,math.e,0.1))
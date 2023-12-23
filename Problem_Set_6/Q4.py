import math

def ivp_solver(f,f_e,a,b,y_a,h):
    y = y_a
    x = a
    while x <= b:
        y = y + h*f(x,y)
        x = x + h
    
    exact = f_e(b)
    error = abs(exact-y)

    return y, exact, error
    
def f(x,y):
    return y-x

def f_e(x):
    return x+1-math.exp(x)/2

print(ivp_solver(f,f_e,0,1,0.5,0.1))
print(ivp_solver(f,f_e,0,1,0.5,0.05))
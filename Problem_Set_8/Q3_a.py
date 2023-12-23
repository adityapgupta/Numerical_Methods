import math

def adam_bashforth_3(f,a,b,y_a,h):
    x = a
    y_0 = y_a
    y_1 = y_0 + h*(f(x,y_0) + 3*f(x+2*h/3, y_0 + 2*h*f(x+h/3, y_0 + h*f(x,y_0)/3)/3))/4

    x = x + h
    y_2 = y_1 + h*(f(x,y_1) + 3*f(x+2*h/3, y_1 + 2*h*f(x+h/3, y_1 + h*f(x,y_1)/3)/3))/4
    
    x = x + h
    for i in range(2, int((b-a)/h)):
        y = y_2 + h*(23*f(x,y_2) - 16*f(x-h,y_1) + 5*f(x-2*h,y_0))/12
        y_0 = y_1
        y_1 = y_2
        y_2 = y
        x = x + h
    return y_2


def f(x,y):
    return (x*math.exp(3*x) - 2*y)

def f_0(x):
    return x*math.exp(3*x)/5 - math.exp(3*x)/25 + math.exp(-2*x)/25 

def g(x,y):
    return (1+(x-y)**2)

def g_0(x):
    return (x + 1/(1-x))

def h(x,y):
    return (1+y/x)

def h_0(x):
    return (x*math.log(x) + 2*x)


print(adam_bashforth_3(f,0,1,0,0.2), abs(adam_bashforth_3(f,0,1,0,0.2)-f_0(1)))
print(adam_bashforth_3(g,2,3,1,0.2), abs(adam_bashforth_3(g,2,3,1,0.2)-g_0(3)))
print(adam_bashforth_3(h,1,2,2,0.2), abs(adam_bashforth_3(h,1,2,2,0.2)-h_0(2)))


import math

def trapezoidal(f,a,b,y_a,h):
    y = y_a
    x = a
    while x < b:
        y = y + h*(f(x,y)+f(x+h,y+h*f(x,y)))/2
        x = x + h
    return y


def f(x,y):
    return (y/x-y**2/x**2)

def g(x,y):
    return (math.sin(x) + math.exp(-x))

def p(x,y):
    return ((y**2+y)/x)

def q(x,y):
    return (-x*y + 4*x/y)

if __name__ == '__main__':
    print(trapezoidal(f,1,2,1,0.1))
    print(trapezoidal(g,0,1,0,0.5))
    print(trapezoidal(p,1,3,-2,0.5))
    print(trapezoidal(q,0,1,1,0.25))

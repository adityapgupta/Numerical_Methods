import math

def taylor_2(f,f_1,a,b,y_a,h):
    y = y_a
    x = a
    while x < b:
        y = y + h*f(x,y) + h**2*f_1(f,x,y)/2
        x = x + h
    return y


def f(x,y):
    return (y/x-y**2/x**2)

def f_1(f,x,y):
    return (-y/x**2 + 2*y**2/x**3 + f(x,y)*(1/x-2*y/x**2))

def g(x,y):
    return (math.sin(x) + math.exp(-x))

def g_1(f,x,y):
    return (math.cos(x) - math.exp(-x))

def p(x,y):
    return ((y**2+y)/x)

def p_1(f,x,y):
    return (-(y**2+y)/x**2 + f(x,y)*(2*y+1)/x)

def q(x,y):
    return (-x*y + 4*x/y)

def q_1(f,x,y):
    return (-y + 4/y + f(x,y)*(-x-4*x/y**2))


if __name__ == '__main__':
    print(taylor_2(f,f_1,1,2,1,0.1))
    print(taylor_2(g,g_1,0,1,0,0.5))
    print(taylor_2(p,p_1,1,3,-2,0.5))
    print(taylor_2(q,q_1,0,1,1,0.25))
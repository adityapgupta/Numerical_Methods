import math

def rk_2(f,a,b,y_a,h):
    y = y_a
    x = a
    while x < b:
        k_1 = h*f(x,y)
        k_2 = h*f(x+h,y+k_1)
        y = y + (k_1+k_2)/2
        x = x + h
    return y

def rk_2_mid(f,a,b,y_a,h):
    y = y_a
    x = a
    while x < b:
        k_1 = h*f(x,y)
        k_2 = h*f(x+h/2,y+k_1/2)
        y = y + k_2
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
    print(rk_2(f,1,2,1,0.1))
    print(rk_2(g,0,1,0,0.5))
    print(rk_2(p,1,3,-2,0.5))
    print(rk_2(q,0,1,1,0.25))

    print(rk_2_mid(f,1,2,1,0.1))
    print(rk_2_mid(g,0,1,0,0.5))
    print(rk_2_mid(p,1,3,-2,0.5))
    print(rk_2_mid(q,0,1,1,0.25))

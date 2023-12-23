import math

def rk_2_coupled(f,a,b,y_a,h):
    y = y_a
    x = a

    for i in range(int((b-a)/h)):
        k_1 = h*f(x,y)[0], h*f(x,y)[1]
        k_2 = h*f(x+h,(y[0]+k_1[0],y[1]+k_1[1]))[0], h*f(x+h,(y[0]+k_1[0],y[1]+k_1[1]))[1]
        y = y[0] + (k_1[0]+k_2[0])/2, y[1] + (k_1[1]+k_2[1])/2
        x = x + h
    return y

def f(x,y):
    return (3*y[0] + 2*y[1] - (2*x**2 + 1)*math.exp(2*x), 4*y[0] + y[1] + (x**2 + 2*x - 4)*math.exp(2*x))

def f_0(x):
    return (math.exp(5*x)/3 - math.exp(-x)/3 + math.exp(2*x), math.exp(5*x)/3 + 2*math.exp(-x)/3 + x**2*math.exp(2*x))

print(rk_2_coupled(f,0,1,(1,1),0.2), abs(rk_2_coupled(f,0,1,(1,1),0.2)[0]-f_0(1)[0]), abs(rk_2_coupled(f,0,1,(1,1),0.2)[1]-f_0(1)[1]))

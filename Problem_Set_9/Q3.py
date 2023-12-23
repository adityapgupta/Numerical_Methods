import math

def non_linear_shooting(f_0,f_1,f_2,a,b,y_a,y_b,h,m,tol):
    t = (y_b-y_a)/(b-a)

    for i in range(m):
        y1 = [(y_a,t)]
        y = y1[0]
        x = a

        for i in range(int((b-a)/h)):
            y = y[0] + h*f_1(x,y)[0], y[1] + h*f_1(x,y)[1]
            x = x + h
            y1.append(y)
        
        z = (0,1)
        x = a

        for i in range(int((b-a)/h)):
            z = z[0] + h*f_2(y1[i],z)[0], z[1] + h*f_2(y1[i],z)[1]
            x = x + h
        
        if abs(y1[-1][0] - y_b) < tol:
            break
        
        t = t - (y1[-1][0] - y_b)/z[0]
    
    for i in range(len(y1)):
        print((y1[i][0], abs(y1[i][0] - f_0(a + i*h))))
    

def f_1(x,y):
    return y[1], (32 + 2*x**3 - y[0]*y[1])/8

def f_2(y,z):
    return z[1], -(y[1]*z[0] + y[0]*z[1])/8

def f_0(x):
    return x**2 + 16/x

if __name__ == '__main__':
    non_linear_shooting(f_0,f_1,f_2,1,3,17,43/3,0.05,10,1e-5)
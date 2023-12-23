import math

def linear_shooting(f_0,f_1,f_2,a,b,y_1,y_2,y_b,h):
    y1 = [y_1]
    y2 = [y_2]
    
    y = y1[0]
    x = a

    for i in range(int((b-a)/h)):
        y = y[0] + h*f_1(x,y)[0], y[1] + h*f_1(x,y)[1]
        x = x + h
        y1.append(y)

    y = y2[0]
    x = a

    for i in range(int((b-a)/h)):
        y = y[0] + h*f_2(x,y)[0], y[1] + h*f_2(x,y)[1]
        x = x + h
        y2.append(y)
    
    y = []
    for i in range(len(y1)):
        y.append(y1[i][0] + (y_b - y1[-1][0])/y2[-1][0]*y2[i][0])

    for i in range(len(y)):
        print((y[i], abs(y[i] - f_0(a + i*h))))


def f_1(x,y):
    return y[1], (-2)*y[1]/x + 2*y[0]/x**2 + math.sin(math.log(x))/x**2

def f_2(x,y):
    return y[1], (-2)*y[1]/x + 2*y[0]/x**2

def f_0(x):
    return 1.139*x - 0.039/x**2 -3*math.sin(math.log(x))/10 - math.cos(math.log(x))/10

if __name__ == '__main__':
    linear_shooting(f_0,f_1,f_2,1,2,(1,0),(0,1),2,0.1)


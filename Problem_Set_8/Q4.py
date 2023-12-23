import math

def adam_predictor_corrector(f,a,b,y_a,h):
    x = a
    y_0 = y_a
    y_values = []

    for i in range(2):
        k_1 = h*f(x,y_0)
        k_2 = h*f(x+h/2,y_0+k_1/2)
        k_3 = h*f(x+h/2,y_0+k_2/2)
        k_4 = h*f(x+h,y_0+k_3)
        y_0 = y_0 + (k_1+2*k_2+2*k_3+k_4)/6
        y_values.append(y_0)
        x = x + h

    y_1, y_2 = y_values[0], y_values[1]

    for i in range(2, int((b-a)/h)):
        k_1 = h*f(x,y_2)
        k_2 = h*f(x+h/2,y_2+k_1/2)
        k_3 = h*f(x+h/2,y_2+k_2/2)
        k_4 = h*f(x+h,y_2+k_3)
        y_3 = y_2 + (k_1+2*k_2+2*k_3+k_4)/6
        
        y = y_2 + h*(9*f(x+h,y_3) + 19*f(x,y_2) - 5*f(x-h,y_1) + f(x-2*h,y_0))/24
        y_0 = y_1
        y_1 = y_2
        y_2 = y_3
        x = x + h
    return y

def f(x,y):
    return (y - x**2 + 1)

print(adam_predictor_corrector(f,0,2,0.5,0.2))
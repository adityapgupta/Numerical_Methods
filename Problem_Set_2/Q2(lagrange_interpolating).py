import matplotlib.pyplot as plt
import numpy as np

def f_calculator(A,f):
    n = len(A)
    f_values = [[f(x) for x in A]]

    for i in range(n-1):
        temp = []
        for j in range(n-i-1):
            value = (f_values[i][j+1]-f_values[i][j])/(A[j+i+1]-A[j])
            temp.append(value)
        f_values.append(temp)

    firsts = [x[0] for x in f_values]
    return firsts

def calculator(x,A,f_values):
    n = len(A)
    result = f_values[0]
    for i in range(1,n):
        temp = 1
        for j in range(i):
            temp *= (x-A[j])
        result += f_values[i]*temp
    return result

def interpolate(f,x0,x1,n):
    A = [x0 + i*(x1-x0)/n for i in range(n+1)]
    f_values = f_calculator(A,f)
    return A, f_values

def f(x):
    return 100*x**6 + 200

A, f_values = interpolate(f,0,1,5)
print(calculator(0.3,A,f_values))

# x = np.linspace(-1,1,1000)
# y1 = [f(x) for x in x]
# y2 = [calculator(x,A,f_values) for x in x]

# plt.plot(x,y1)
# plt.plot(x,y2)
# plt.show()

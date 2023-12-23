import numpy as np
import matplotlib.pyplot as plt

def linear_difference(f,a,b,y_0,y_1,n):
    h = 1/(n+1)
    x = np.linspace(0,1,n+2)

    A = np.zeros((n,n))
    L = np.zeros(n)

    L[0] += h**2*f(x[1])/a + y_0
    L[n-1] += h**2*f(x[n])/a + y_1
    for i in range(1,n-1):
        L[i] += h**2*f(x[i+1])/a
    
    for i in range(n):
        A[i,i] += 2 + b*h**2*(1+x[i+1]**2)/a
        if i < n-1:
            A[i,i+1] += -1
            A[i+1,i] += -1
    
    print(L)
    return A,L
        

def gauss_jacobi(A,L,x_0,tol=1e-5):
    n = len(A)
    x = x_0
    x_new = np.zeros(n)
    i = 0
    max_diff = 1

    while max_diff > tol:
        for j in range(n):
            x_new[j] = (L[j] - np.dot(A[j][:j],x[:j]) - np.dot(A[j][j+1:],x[j+1:]))/A[j][j]
        
        max_diff = max([abs(x_new[i] - x[i]) for i in range(n)])
        x = x_new.copy()
        i += 1
    
    print(max_diff)
    print(i)
    return x_new


def gauss_seidel(A,L,x_0,tol=1e-5):
    n = len(A)
    x = x_0
    x_new = np.zeros(n)
    i = 0
    max_diff = 1

    while max_diff > tol:
        for j in range(n):
            x_new[j] = (L[j] - np.dot(A[j][:j],x_new[:j]) - np.dot(A[j][j+1:],x[j+1:]))/A[j][j]

        max_diff = max([abs(x_new[i] - x[i]) for i in range(n)])

        x = x_new.copy()
        i += 1

    print(max_diff)
    print(i)
    return x_new


def f(x):
    return -64*(12*x**2 -12*x +2) + (1+x**2)*64*x**2*(1-x)**2

def y(x):
    return 64*x**2*(1-x)**2

A,L = linear_difference(f,1,1,0,0,49)
jacobi = gauss_jacobi(A,L,[0]*49,1e-3)
seidel = gauss_seidel(A,L,[0]*49,1e-3)

x_values = np.linspace(0,1,29+2)
y_values = [y(x) for x in x_values[1:-1]]

plt.plot(x_values[1:-1],y_values, 'r')
plt.plot(x_values[1:-1],jacobi, 'g')
plt.plot(x_values[1:-1],seidel, 'b')
plt.legend(['Analytical', 'Jacobi', 'Seidel'])

plt.show()

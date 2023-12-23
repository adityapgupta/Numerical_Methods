def composite_trapezoidal(f,a,b,n):
    h = (b-a)/n
    
    s = 0
    for i in range(1,n):
        s += f(a+i*h)

    integral =  h*(f(a)+2*s+f(b))/2
    error = abs(integral - 1100/3)

    return integral, error

def composite_simpson(f,a,b,n):
    h = (b-a)/n
    
    s = 0
    for i in range(1,n):
        s += f(a+i*h)
    s *= 2

    t = 0
    for i in range(1,n+1):
        t += f(a+(i-0.5)*h)
    t *= 4

    integral =  h*(f(a)+s+t+f(b))/6
    error = abs(integral - 1100/3)

    return integral, error

def f(x):
    return x**3 + 5*x**2 + 1

print(composite_trapezoidal(f,1,5,5))
print(composite_trapezoidal(f,1,5,10))

print(composite_simpson(f,1,5,5))
print(composite_simpson(f,1,5,10))
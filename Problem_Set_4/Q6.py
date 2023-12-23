def composite_trapezoidal(f,a,b,n):
    h = (b-a)/n
    
    s = 0
    for i in range(1,n):
        s += f(a+i*h)

    integral =  h*(f(a)+2*s+f(b))/2
    error = abs(integral - 15/4)

    return integral, error

def f(x):
    return x**3

print(composite_trapezoidal(f,1,2,4))
print(composite_trapezoidal(f,1,2,8))
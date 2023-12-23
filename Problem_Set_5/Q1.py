def composite_rectangular(f,a,b,n):
    h = (b-a)/n
    
    s = 0
    for i in range(n):
        s += f(a+i*h)

    integral =  h*(s)
    error = abs(integral - 1100/3)

    return integral, error

def composite_midpoint(f,a,b,n):
    h = (b-a)/n
    
    s = 0
    for i in range(n):
        s += f(a+i*h+h/2)

    integral =  h*(s)
    error = abs(integral - 1100/3)

    return integral, error

def f(x):
    return x**3 + 5*x**2 + 1

print(composite_rectangular(f,1,5,5))
print(composite_rectangular(f,1,5,10))

print(composite_midpoint(f,1,5,5))
print(composite_midpoint(f,1,5,10))
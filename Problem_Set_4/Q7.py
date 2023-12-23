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
    error = abs(integral - 15/4)

    return integral, error

def f(x):
    return x**3

print(composite_simpson(f,1,2,4))
print(composite_simpson(f,1,2,8))

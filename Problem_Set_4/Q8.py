import math

def composite_trapezoidal(f,a,b,n):
    h = (b-a)/n
    
    s = 0
    for i in range(1,n):
        s += f(a+i*h)

    integral =  h*(f(a)+2*s+f(b))/2
    error = (b-a)*(h**2)/12

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
    error = (b-a)*(h**4)/(180*2**4)

    return integral, error

def true_value(f,a,b,n):
    h = (b-a)/n
    
    s = 0
    for i in range(n):
        s += f(a+i*h)
    s *= h

    return s

def f(x):
    return math.exp(x**2)


exact = true_value(f,0,2,10000)

trapezoidal, e1 = composite_trapezoidal(f,0,2,4)
simpson, e2 = composite_simpson(f,0,2,4)

print(exact)
print(trapezoidal, abs(exact-trapezoidal), e1*982.7667005966) # f2 = (4x^2+2)*exp(x^2)
print(simpson, abs(exact-simpson), e2*25115.149015246345) # f4 = (16x^4+48x^2+12)*exp(x^2)
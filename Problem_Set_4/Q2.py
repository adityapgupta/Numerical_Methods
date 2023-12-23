def trapezoid(f,a,b):
    return (b-a)*(f(a)+f(b))/2 

def f(x):
    return (1+x**2)**(0.5)

print(trapezoid(f,1,5))
def rectangular(f,a,b):
    return (b-a)*f(a)

def midpoint(f,a,b):
    return (b-a)*f((a+b)/2)

def f(x):
    return (1+x**2)**(0.5)

print(rectangular(f,1,5))
print(midpoint(f,1,5))
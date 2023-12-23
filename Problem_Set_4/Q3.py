def simpson(f, a, b):
    return (b-a)*(f(a)+4*f((a+b)/2)+f(b))/6

def f(x):
    return 1/(3-x**(0.5))

print(simpson(f, 4, 6))
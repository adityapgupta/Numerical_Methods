import math

def simpson(f,a,b,c,d):
    return (b-a)*(d-c)/36*(f(a,c)+f(a,d)+f(b,c)+f(b,d)+4*f((a+b)/2,c)+4*f((a+b)/2,d)+4*f(a,(c+d)/2)+4*f(b,(c+d)/2)+16*f((a+b)/2,(c+d)/2))

def f(x,y):
    return math.log(x+2*y) 

def composite_simpson(f,a,b,c,d,n,m):
    h = (b-a)/n
    k = (d-c)/m
    
    s = 0
    for i in range(n):
        for j in range(m):
            x = a+i*h
            y = c+j*k
            s += simpson(f,x,x+h,y,y+k)
    
    return s

print(composite_simpson(f,1.4,2.0,1.0,1.5,4,2))
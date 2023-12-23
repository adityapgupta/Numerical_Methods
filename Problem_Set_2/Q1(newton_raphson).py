import math

def newton(f,f1,x0,eps):
	x = x0
	while abs(f(x)) > eps:
		x = x - f(x)/f1(f,x,eps)
	return x

def f0(x):
	return math.e**x - x**3

def f(x):
	return math.e**x - 3*x**2

def f1(f,x,tol):
	return (f(x+tol) - f(x))/tol

values = []
for i in range(-5,6):
	values.append(newton(f,f1,i,1e-10))

f_values = [f0(x) for x in values]
print(min(f_values))
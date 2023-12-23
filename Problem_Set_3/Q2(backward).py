import math

def delta_values(A):
    values = []
    values.append(A)

    for i in range(len(A)-1):
        temp = []
        for j in range(len(A)-i-1):
            value = values[i][j]-values[i][j-1]
            temp.append(value)
        values.append(temp)
    
    firsts = [x[0] for x in values]
    return firsts

def choose(s,k):
    result = (-1)**k
    for i in range(k):
        result *= (s+i)
    result = result/math.factorial(k)

    return result

def calculator(x,A,n):
    firsts = delta_values(A[1])
    s = (x-A[0][0])/(A[0][0]-A[0][1])

    result = A[1][0]
   
    for k in range(1,n):
        temp = (-1)**k
        temp *= choose(-s,k)
        temp *= firsts[k]
        result += temp
    
    return result


print(calculator((-1/3), [[0, -0.25, -0.5, -0.75], [1.10100000, 0.33493750, -0.02475000,-0.07181250]],4))
print(calculator((0.25), [[0.1, 0.2, 0.3, 0.4], [-0.62049958, -0.28398668, 0.00660095, 0.24842440]],4))

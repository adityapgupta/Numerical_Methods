import numpy as np  

def linear_row(A_1,A_2,k):
    for i in range(len(A_1)):  
        A_1[i] += k*A_2[i]
    return A_1

def gauss_elimination(A,b):
    n = len(A)
    for i in range(n-1):
        p = 0
        while A[i][p] == 0 and p < n:
            p += 1
        if p == n:
            print("No unique solution exists")
            return
        if p != i:
            A[p], A[i] = A[i], A[p]
            b[p], b[i] = b[i], b[p]
        
        for j in range(i+1,n):
            k = -A[j][i]/A[i][i]
            A[j] = linear_row(A[j],A[i],k)
            b[j] = b[j] + k*b[i]
            print(A)
            print(b)

    if A[n-1][n-1] == 0:
        print("No unique solution exists")
        return
    
    print(A)
    print(b)
    x = np.zeros(n)
    x[n-1] = b[n-1]/A[n-1][n-1]

    for i in range(n-2,-1,-1):
        x[i] = (b[i] - np.dot(A[i][i+1:],x[i+1:]))/A[i][i]
    return x

A = [[4,-1,1],[2,5,2],[1,2,4]]
b = [8,3,11]

print(gauss_elimination(A,b))
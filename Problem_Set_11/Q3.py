import numpy as np

def gauss_seidel(A,b,x_0):
    n = len(A)
    x = x_0
    x_new = np.zeros(n)

    while True:
        for j in range(n):
            x_new[j] = (b[j] - np.dot(A[j][:j],x[:j]) - np.dot(A[j][j+1:],x[j+1:]))/A[j][j]

        diff = [abs(x_new[i] - x[i]) for i in range(n)]
        print(diff)
        if max(diff) < 1e-5:
            break
        x = x_new

    return x_new


A = np.array([[10,-1,2,0],[-1,11,-1,3],[2,-1,10,-1],[0,3,-1,8]])
b = np.array([6,25,-11,15])

if __name__ == "__main__":
    print(gauss_seidel(A,b,[0,0,0,0]))
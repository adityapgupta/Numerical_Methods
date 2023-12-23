def fixed_point(f, x0, tol=1e-4, maxiter=1000):
    x = x0
    for i in range(maxiter):
        fx = f(x)
        if abs(fx-x) < tol:
            return x
        x = fx
    return "No solution found"

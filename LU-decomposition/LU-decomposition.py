import numpy as np

def lu_decomposition(M):
    # Dimension
    n = M.shape[0]

    # Init L and U
    L = np.eye(n)  
    U = M.copy() 
    
    # Gauss Elimination
    for i in range(n):

        # Check if the factor calculation is possible. Notice a / b is possible since b != 0.
        if U[i, i] == 0.0:
            raise ValueError("Division by zero error. LU decomposition cannot proceed because U[i, i] is zero.")

        
        # Gauss Elimination
        for j in range(i+1, n):
            # Mult. factor value
            factor = U[j, i] / U[i, i]
            
            # Updates L
            L[j, i] = factor
            
            # Updates the row j of U
            U[j, :] = U[j, :] - factor * U[i, :]
    
    return L, U


def solve_linear_system(A, b):
    # Getting the L and U matrices
    L, U = lu_decomposition(A)

    print("Matrix L:")
    print(L)
    print("\nMatrix U:")
    print(U)


    # Solve Ly = b
    y = np.zeros_like(b, dtype='float')
    for i in range(len(b)):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Solve Ux = y
    x = np.zeros_like(b, dtype='float')
    for i in range(len(b) - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


A = np.array([
    [1, 6, 2, 4],
    [3, 19, 4, 15],
    [1, 4, 8, -12],
    [5, 33, 9, 3]
], dtype="float")

b = np.array([8, 25, 18, 72])

solution = solve_linear_system(A, b)
print("\nSolution:", solution, '\n')

# Possible LU decomposition.
# M = np.array([
#     [1, 6, 2, 4],
#     [3, 19, 4, 15],
#     [1, 4, 8, -12],
#     [5, 33, 9, 3]
# ], dtype="float")

# Impossible LU decomposition - Throws an error.
# M = np.zeros((4, 4))

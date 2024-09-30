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
            print(U[j, :])
            print(U[i, :])
            
            U[j, :] = U[j, :] - factor * U[i, :]
    
    return L, U


M = np.array([
    [1, 6, 2, 4],
    [3, 19, 4, 15],
    [1, 4, 8, -12],
    [5, 33, 9, 3]
], dtype="float")


L, U = lu_decomposition(M)

print("Matrix L:")
print(L)
print("\nMatrix U:")
print(U)

# Possible LU decomposition.
# M = np.array([
#     [1, 6, 2, 4],
#     [3, 19, 4, 15],
#     [1, 4, 8, -12],
#     [5, 33, 9, 3]
# ], dtype="float")

# Impossible LU decomposition - Throws an error.
# M = np.zeros((4, 4))

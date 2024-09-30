import numpy as np

def lu_decomposition(M):

    # Singular Verification
    isSingular = np.linalg.det(M) == 0
    if(isSingular):
        raise ValueError("It is not possible to perform the LU decomposition on singular matricies")
    
    # Dimension
    n = M.shape[0]

    # Init L and U
    L = np.eye(n)  
    U = M.copy() 
    
    # Gauss Elimination
    for i in range(n):
        
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

import numpy as np

def qr_decomposition_classical(vectors):
    Q = np.zeros_like(vectors, dtype=float)
    R = np.zeros((vectors.shape[1], vectors.shape[1]), dtype=float)

    for i in range(vectors.shape[1]):
        vector = vectors[:, i]
        
        for j in range(i):
            R[j, i] = np.dot(Q[:, j], vector)
            vector -= R[j, i] * Q[:, j]
        
        R[i, i] = np.linalg.norm(vector)
        Q[:, i] = vector / R[i, i]
    
    return Q, R


A = np.array([[1, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=float).T
Q, R = qr_decomposition_classical(A)

print("Q - Orthonormal Basis:\n", np.round(Q, 3))
print("\nR - Upper Triangular Matrix:\n", np.round(R, 3))

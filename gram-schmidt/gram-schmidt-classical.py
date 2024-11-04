import numpy as np

def gram_schmidt_classical(vectors, orthonormalize=False):
    orthogonal_vectors = np.zeros_like(vectors, dtype=float)
    
    for i in range(vectors.shape[1]):
        vector = vectors[:, i]
        
        for j in range(i):
            proj = np.dot(orthogonal_vectors[:, j], vector) / np.dot(orthogonal_vectors[:, j], orthogonal_vectors[:, j])
            vector -= proj * orthogonal_vectors[:, j]

        orthogonal_vectors[:, i] = vector
        
        if orthonormalize:
            orthogonal_vectors[:, i] /= np.linalg.norm(orthogonal_vectors[:, i])
    
    return orthogonal_vectors


vectors = np.array([[1, 1, 1], [1, -1, 1], [-1, 0, 1]], dtype=float).T
orthonormal_basis = np.round(gram_schmidt_classical(vectors, orthonormalize=True), 3)

print("Classical Gram-Schmidt Approach:\n", orthonormal_basis)
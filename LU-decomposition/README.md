# LU-decomposition

## General Idea
Any square matrix M can be written as the product of two matrices, M = LU, where L is a lower triangular matrix and U is an upper triangular matrix.

- Upper triangular matrix: \( a_ij = 0 \) when \( j > i \).

- Lower triangular matrix: \( a_ij = 0 \) when \( j < i \).

## Why use it might be a good idea?
LU decomposition simplifies solving linear systems, matrix inversion, and determinant calculation more efficiently.

### Algorithm

1. **Write M as the product of two matrices**: M = LU.

2. **Starting point**: Write M in the simplest way possible, M = I * M, where I is the identity matrix. So, L = I and U = M.

3. **Gaussian elimination on U**:
   3.1. The goal is to reduce U (zero out the elements below the diagonal).
   
   3.2. After each elimination at position ij, record the multiplier used at position ij in matrix L.
   
   3.3. This way, we obtain new versions of L and U, called Lk and Uk, where M = L_k * U_k.
   
   3.4. Stop when some U_k is fully reduced (in upper triangular form).

4. **End**.

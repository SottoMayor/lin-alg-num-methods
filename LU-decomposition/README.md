# LU-decomposition

## General Idea
Any square matrix M can be written as the product of two matrices, M = LU, where L is a lower triangular matrix and U is an upper triangular matrix.

- Upper triangular matrix: \( a_ij = 0 \) when \( j > i \).

- Lower triangular matrix: \( a_ij = 0 \) when \( j < i \).

## Why use it might be a good idea?
LU decomposition simplifies solving linear systems, matrix inversion, and determinant calculation more efficiently.

## Algorithm

1. **Write M as the product of two matrices**: M = LU.

2. **Starting point**: Write M in the simplest way possible, M = I * M, where I is the identity matrix. So, L = I and U = M.

3. **Gaussian elimination on U**:   
   3.1. The goal is to reduce U (zero out the elements below the diagonal).
   
   3.2. After each elimination at position ij, record the multiplier used at position ij in matrix L.
   
   3.3. This way, we obtain new versions of L and U, called Lk and Uk, where M = L_k * U_k.
   
   3.4. Stop when some U_k is fully reduced (in upper triangular form).

4. **End**.

## Steps for Solving the System

1. **Decomposition of M**:
   The first step is to decompose the matrix  M  into L and  U :   
   `M = LU`

2. **Forward Substitution to Solve for  y**:
   Solve the equation  `Ly = b`. This is done using forward substitution, for each row `i` of `L` , we compute `y[i]`:
   - For each entry `y[i]`  is computed as the value of `b[i]` minus the sum of the products of the known values of `L[i, j]` and  `y[j]`  for all  `j < i` .

3. **Backward Substitution to Solve for x**:
   Once we have  `y` , we solve the equation  `Ux = y` using backward substitution. For each row `i` of `U` , we compute  `x[i]` as:
   - For each entry `x[i]`  is calculated as the difference between `y[i]` and the sum of the products of the known values of `U[i, j]` and `x[j]` for all `j > i`, divided by the diagonal entry `U[i,i]`.

## Algorithm Weakness: Handling Zeros on the Diagonal

A weakness of this LU decomposition algorithm is its inability to handle cases where a diagonal element of matrix U is zero during iterations. When  U[i, i] = 0 , a division by zero occurs, causing the decomposition process to fail, even if the original matrix is not singular. To address this issue, implementing **partial pivoting** is recommended.

# QR Decomposition

The QR decomposition (also known as QR factorization) is a method for decomposing a matrix into two parts: an orthogonal matrix and an upper triangular matrix. For a given real square matrix **A**, the QR decomposition expresses **A** as:

**A = QR**

where:
- **Q** is an orthogonal matrix (meaning **Q' Q = I**),
- **R** is an upper triangular matrix.

If **A** is nonsingular, this factorization is unique.

## Gram-Schmidt Process for QR Factorization

One approach to compute the QR decomposition is through the **Gram-Schmidt process**. In this method, we treat the columns of matrix **A** as the vectors to be orthogonalized.

Given:
**A = [ a1 | a2 | ... | an ]**

The process constructs orthogonal vectors **u1, u2, ..., un** and their normalized counterparts **e1, e2, ..., en** (which form the columns of **Q**) as follows:

1. **Initialize**:
   - Set **u1 = a1**
   - Define **e1 = u1 / ||u1||**

2. **Iterative Orthogonalization**:
   - For each **k = 2, ..., n**:
     - Compute **uk = ak - (ak · e1)e1 - ... - (ak · ek-1)ek-1**
     - Normalize to get **ek = uk / ||uk||**

In this process, **|| · ||** denotes the **L2 norm**.

## Constructing the QR Factorization

After obtaining the orthonormal vectors **e1, ..., en**, the matrix **Q** can be formed by using these vectors as columns. The matrix **R** is created by calculating the projection coefficients of each **ai** onto each **ei**.

Thus, **A** can be expressed as:

**A = [ e1 | e2 | ... | en ]**
  
And **R** is the matrix of projections:

[[ a1 · e1, a2 · e1, ..., an · e1 ],
 [ 0,      a2 · e2, ..., an · e2 ],
 [ ...,     ...,    ...,        ],
 [ 0,      0,        ..., an · en ]]

Therefore:

**A = QR**

Once **e1, ..., en** are computed, the QR factorization is straightforward to write down.

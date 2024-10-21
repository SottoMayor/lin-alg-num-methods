import numpy as np

def gauss_elimination(A, b):
    # matrix A and b array
    n = len(b)
    A = np.hstack([A, b.reshape(-1, 1)])

    # Step 3 - Echelon process
    for i in range(n):
        # Step 1 - Pivot
        A[i] = A[i] / A[i][i]

        # Step 2 - Elimination below pivot
        for k in range(i + 1, n):
            A[k] = A[k] - A[k][i] * A[i]

    # print A echelon form
    print('\nMatrix A:')
    for row in A[:, :-1]:  # Ignora a última coluna de b
        print(" ".join(f"{elem:.2f}" for elem in row))
    print('\n')

    # Step 4 - Back Substitution
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = A[i][-1] - np.dot(A[i][i+1:n], x[i+1:n])

    return x


if __name__ == "__main__":
    # Important: Set the A and b as float matrix.
    A = np.array([[1, -3, 2], [-2, 8, -1], [4, -6, 5]], dtype=float)
    b = np.array([11, -15, 29], dtype=float)

    # Solve
    sol = gauss_elimination(A, b)

    print("System solution:", sol)


# A = np.array([[1, 6, 2, 4], [3, 19, 4, 15], [1, 4, 8, -12], [5, 33, 9, 3]], dtype=float)
# b = np.array([8, 25, 18, 72], dtype=float)

#  A = np.array([[9, 6, -3, 3], [6, 20, 2, 22], [-3, 2, 6, 2], [3, 22, 2, 28]], dtype=float)
#     b = np.array([12, 64, 4, 82], dtype=float)
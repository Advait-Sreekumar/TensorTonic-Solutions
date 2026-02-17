import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A=np.array(A)
    rows, colums= A.shape
    t= np.zeros((colums,rows))
    for i in range(rows):
        for j in range(colums):
            t[j,i]=A[i,j]

    return t
    pass

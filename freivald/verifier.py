import numpy as np
from random import randrange

def verify_matrix_multiplication(A: list[list[int]], B: list[list[int]], C: list[list[int]]) -> bool:
    '''
    Returns True if A*B is equal to C and False otherwise (with high probability).
    '''
    # TODO: operations should be modulo the prime
    # So we would have to convert the arrays...
    prime = 683
    n = len(A)
    A_arr = np.array(A)
    B_arr = np.array(B)
    C_arr = np.array(C)

    # Pick a random r in range [0, prime)
    r = randrange(0, prime)
    # make a vector [1, r, r^2, ..., r^{n-1}] and convert it to a numpy array
    x_arr = np.array(create_vector(n, prime, r))

    # multiply C * x
    y = np.matmul(C_arr, x_arr)
    
    # calculate A*(B*x)
    z = np.matmul(A_arr, np.matmul(B_arr, x_arr))

    return (y == z).all()

def create_vector(n: int, prime: int, r: int) -> list[int]:
    '''
    Returns the list [1, r, r^2, ..., r^{n-1}]
    '''
    # make a vector [1, r, r^2, ..., r^{n-1}]
    x = []
    elem = 1
    for i in range(n):
        x.append(elem)
        elem = elem * r
    return x
"""
Exercise 3.4, p. 32
"""

import math

p = 11

class Field:
    def __init__(self, p) -> None:
        self.p = p
    
    def add(self, a: int, b: int) -> int:
        return (a % self.p + b % self.p) % p
    
    def mult(self, a: int, b: int) -> int:
        return ((a % self.p) * (b % self.p)) % self.p

class FunctionEvaluation:

    def __init__(self, evals: list[int], p: int) -> None:
        self.field = Field(p)
        log = int(math.log(len(evals), 2))
        if (2**log == len(evals)):
            self.evals = evals
        else:
            raise ValueError #TODO: fix the error
        

    def evaluate(self, r: list[int]) -> int:
        n = len(self.evals)
        log = int(math.log(n, 2))
        x = [] # this is multilinear Langrange basis polynomials with interpolating set {0,1}^n
        for i in range(n):
            prod = 1
            # take binary representation
            b = bin(i)
            # deal with missing zeroes in the beginning of string
            for j in range(log-len(b)):
                prod *= 1 - r[i]
            # calculate the rest
            for bit in b:
                if bit == "1":
                    prod *= r[i]
                else:
                    prod *= 1 - r[i]
            x.append(prod)
        # now calculate sum
        sum = 0
        for i in range(n):
            sum += self.evals[i]*x[i]
        return sum % self.p #TODO: make this more efficient by using the class
    
if __name__ == "__main__":
    evals = [3, 4, 1, 2]
    test = FunctionEvaluation(evals, 11)
    test.evaluate([2, 4])                               
        




    
    
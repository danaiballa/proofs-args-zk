"""
Exercise 3.4, p. 32
"""

import math

p = 11

# TODO: make a class for field element

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
            # TODO: find a better name than 'log'
            self.log = log
        else:
            raise ValueError #TODO: fix the error
            
    def slow_evaluate(self, input: list[int]) -> int:
        n = len(self.evals)
        lagrange_basis_evals = [] # this is multilinear Langrange basis polynomials with interpolating set {0,1}^n
        #TODO: perhaps make an array of all the basis. Not the best, since we are using more space, but more readable
        for i in range(n):
            prod = 1
            # take binary representation
            basis_elem = self.__binarize(i)
            # calculate the rest
            for bit in basis_elem:
                if bit == "1":
                    prod = self.field.mult(prod, self.evals[i])
                else:
                    prod = self.field.mult(prod, 1-self.evals[i])
            lagrange_basis_evals.append(prod)
        # now calculate sum
        sum = 0
        for i in range(n):
            sum = self.field.add(sum, self.field.mult(self.evals[i], lagrange_basis_evals[i]))
        return sum
    
    def __binarize(self, num: int)-> str:
        b = bin(num)
        # Add missing 0's and return
        return "0"*(self.log - len(b)) + b
    
if __name__ == "__main__":
    evals = [3, 4, 1, 2]
    test = FunctionEvaluation(evals, 11)
    evaluation = test.slow_evaluate([2, 4])   
    print(evaluation)                       
        




    
    
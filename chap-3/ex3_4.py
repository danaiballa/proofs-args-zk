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

    def __init__(self, f_evals: list[int], p: int) -> None:
        self.field = Field(p)
        log = int(math.log(len(f_evals), 2))
        if (2**log == len(f_evals)):
            self.f_evals = f_evals
            # TODO: find a better name than 'log'
            self.log = log
        else:
            raise ValueError #TODO: fix the error
            
    def slow_evaluate(self, input: list[int]) -> int:
        lagrange_basis_evals = self.find_lagnrange_basis_evals(input)
        # now calculate sum
        sum = 0
        n = len(self.f_evals)
        for i in range(n):
            sum = self.field.add(sum, self.field.mult(self.f_evals[i], lagrange_basis_evals[i]))
        return sum
    
    def find_lagnrange_basis_evals(self, input: list[int]) -> list[int]:
        n = len(self.f_evals)
        lagrange_basis_evals = [] # this is multilinear Langrange basis polynomials with interpolating set {0,1}^n
        for i in range(n):
            prod = 1
            # take binary representation
            basis_elem = self.__binarize(i)
            # calculate the basis polynomial evaluation for this basis element
            for j in range(self.log):
                coordinate = basis_elem[j]
                if coordinate == "1":
                    prod = self.field.mult(prod, input[j])
                else:
                    prod = self.field.mult(prod, 1-input[j])
            lagrange_basis_evals.append(prod)
        return lagrange_basis_evals
    
    def __binarize(self, num: int)-> str:
        """
        Binary representation of a number with leading 0's
        """
        b = bin(num)[2:] # binary starts with "0b" so we cut that
        # Add missing 0's and return
        return "0"*(self.log - len(b)) + b
    
if __name__ == "__main__":
    evals = [3, 4, 1, 2]
    test = FunctionEvaluation(evals, 11)
    evaluation = test.slow_evaluate([2, 4])   
    print(evaluation)                       
        




    
    
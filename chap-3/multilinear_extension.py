"""
Exercise 3.4, p. 32
"""

import math

class Field:
    def __init__(self, p) -> None:
        self.p = p
    
    def add(self, a: int, b: int) -> int:
        """
        Add two elements mod p.
        """
        return (a % self.p + b % self.p) % self.p
    
    def mult(self, a: int, b: int) -> int:
        """
        Multiply two elements mod p.
        """
        return ((a % self.p) * (b % self.p)) % self.p
    

class MultilinearExtension:

    def __init__(self, f_evals: list[int], p: int) -> None:
        self.field = Field(p)
        log = int(math.log(len(f_evals), 2))
        if (2**log == len(f_evals)):
            self.f_evals = f_evals
            # TODO: find a better name than 'log'
            self.log = log
        else:
            raise ValueError #TODO: fix the error
 
    def evaluate(self, lagrange_basis_evals: list[int]) -> int:
        sum = 0
        n = len(self.f_evals)
        for i in range(n):
            sum = self.field.add(sum, self.field.mult(self.f_evals[i], lagrange_basis_evals[i]))
        return sum

    def slow_find_lagrange_basis_evals(self, input: list[int]) -> list[int]:
        n = len(self.f_evals)
        lagrange_basis_evals = []
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
    
    def fast_find_lagrange_basis_evals(self, input: list[int]) -> list[int]:
        n = len(input)
        if n == 0: return []
        lagrange_basis_evals = [self.field.add(1, (-1)*input[0]), input[0]]
        for i in range(1, n):
            temp = []
            for eval in lagrange_basis_evals:
                temp.append(self.field.mult(eval, 1-input[i]))
                temp.append(self.field.mult(eval, input[i]))
            lagrange_basis_evals = temp
        return lagrange_basis_evals
                
    def __binarize(self, num: int)-> str:
        """
        Binary representation of a number, with leading 0's

        Example: self.log = 4, num = 3: '0010'
        """
        b = bin(num)[2:] # binary starts with "0b" so we cut that
        # Add missing 0's and return
        return "0"*(self.log - len(b)) + b
    
                    
        




    
    
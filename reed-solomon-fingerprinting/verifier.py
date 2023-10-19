import math

class Verifier:
    '''
    Bob, the verifier, checks whether their sequence is equal to Alice's
    '''
    def __init__(self, sequence: list[int]) -> None:
        # we support sequences of length <= 26
        prime = 683
        if len(sequence) >= math.sqrt(prime):
            raise ValueError
        self.sequence = sequence
        self.prime = prime
    
    def verify(self, r: int, proof: int) -> bool:
        # check if prime is big enough
        sum = 0
        x = r
        n = len(self.sequence)
        for i in range(n):
            sum = (sum + self.sequence[i] * x) % self.prime
            x = (x * r) % self.prime
        return (sum == proof)


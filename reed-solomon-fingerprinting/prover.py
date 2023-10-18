import random

class Prover:
    '''
    Alice, the prover, wants to convince Bob, the verifier, that their sequences are equal.
    Note: we are using a non-secure random number generator (std random).

    In reality, Prover would pick the prime as well.
    Here we hardcode the prime to 683, so we support sequences of length <= 26
    
    '''

    def __init__(self, sequence: list[int]) -> None:
        prime = 683
        if len(sequence) > 26 or max(sequence) > prime:
            raise ValueError
        self.sequence = sequence
        self.prime = prime

    def prove(self) -> (int, int):
        '''
        Returns (random element, proof).
        '''
        # take a random number in range [0, p)
        r = random.randint(0, self.prime)
        # if sequence = [a_1,..., a_n], calculate evaluation of polynomial
        # with coefficients a_1,.., a_n
        sum = 0
        x = r
        n = len(self.sequence)
        for i in range(n):
            sum = (sum + self.sequence[i] * x) % self.prime
            x = (x * r) % self.prime
        return (r, sum)
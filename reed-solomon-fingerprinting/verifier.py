class Verifier:
    '''
    Bob, the verifier, checks whether their sequence is equal to Alice's
    '''
    def __init__(self, sequence: list[int]) -> None:
        self.sequence = sequence
    
    def verify(self, r: int, proof: int, prime: int) -> bool:
        sum = 0
        x = r
        n = len(self.sequence)
        for i in range(n):
            sum = (sum + self.sequence[i] * x) % prime
            x = (x * r) % prime
        return (sum == proof)


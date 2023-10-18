import unittest
from prover import Prover
from verifier import Verifier

class TestReedSolomon(unittest.TestCase):

    def test_equal_sequences(self):
        # note: algorithm is probabilistic so the test may fail
        # but the probability is veeery low
        sequence = [5, 6, 3, 7, 8, 8, 90, 10, 22]
        alice = Prover(sequence)
        bob = Verifier(sequence)

        (r, proof) = alice.prove()
        result = bob.verify(r, proof, alice.prime)
        self.assertTrue(result)
        

    def test_non_equal_sequences(self):
        sequence_1 = [5, 6, 3, 7, 8, 8, 90, 10, 22]
        sequence_2 = [10, 6, 5, 7, 0, 8, 91, 10, 35]
        alice = Prover(sequence_1)
        bob = Verifier(sequence_2)

        (r, proof) = alice.prove()
        result = bob.verify(r, proof, alice.prime)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
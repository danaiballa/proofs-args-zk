import unittest
from ex3_4 import Field, FunctionEvaluation

class TestField(unittest.TestCase):

    def test_add(self):
        field = Field(11)
        a = 5
        b = 10
        result = field.add(a, b)
        self.assertEqual(4, result)

    def test_add_negative(self):
        field = Field(11)
        a = -10
        b = 5
        result = field.add(a, b)
        self.assertEqual(6, result)

class TestLagrangeBasisEvals(unittest.TestCase):
    def test_lagrange_basis_evals(self):
        f_evals = [3, 4, 1, 2]
        test = FunctionEvaluation(f_evals, 11)
        lagrange_basis_evals = test.find_lagnrange_basis_evals([2,4])
        self.assertEqual(lagrange_basis_evals, [3, 7, 5, 8])

if __name__ == '__main__':
    unittest.main()




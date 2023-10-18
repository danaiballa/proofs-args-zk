import unittest
from ex3_4 import Field, MultilinearExtension

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

class TestMultilinearExtension(unittest.TestCase):

    #TODO: test with more test cases + test final result
    def test_slow_evaluation_1(self):

        f_evals = [3, 4, 1, 2]
        prime = 11
        multilinear_extension = MultilinearExtension(f_evals, prime)

        input = [2, 4]
        lagrange_basis_evals = multilinear_extension.slow_find_lagnrange_basis_evals(input)
        result = multilinear_extension.slow_evaluate(input)

        self.assertEqual(lagrange_basis_evals, [3, 7, 5, 8])
        self.assertEqual(result, 3)

    def test_slow_evaluation_2(self):

        f_evals = [1, 5, 2, 6, 3, 7, 4, 8, 12, 10, 2, 6, 8, 11, 4, 5]
        prime = 17
        multilinear_extension = MultilinearExtension(f_evals, prime)

        input = [2,4,6,8]
        result = multilinear_extension.slow_evaluate(input)

        self.assertEqual(result, 13)


if __name__ == '__main__':
    unittest.main()




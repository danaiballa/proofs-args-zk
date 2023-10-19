import unittest
from verifier import verify_matrix_multiplication, create_vector

class TestCreateVector(unittest.TestCase):

    def test_create_vector(self):
        r = 5
        n = 4
        prime = 683
        expected_result = [1, 5, 25, 125]
        result = create_vector(n, prime, r)
        self.assertEqual(result, expected_result)

class TestVerifyMatrixMultiplication(unittest.TestCase):

    def test_verify_matrix_multiplication_correct_1(self):

        A = [[1, 2, 3],
            [5, 6, 7], 
            [4, 6, 8]]
        
        B = [[1, 0, 0],
            [0, 1, 0],
            [0, 0, 1]]
        
        C = list.copy(A)

        result = verify_matrix_multiplication(A, B, C)
        self.assertTrue(result)

    def test_verify_matrix_multiplication_correct_2(self):

        A = [[1, 2, 3],
            [5, 6, 7], 
            [4, 6, 8]]
        
        B = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
        
        # this is correct result
        C = [[30, 36, 42],
             [78, 96, 114],
             [84, 102, 120]]
        
        result = verify_matrix_multiplication(A, B, C)
        self.assertTrue(result)
        

    def test_verify_matrix_multiplication_wrong(self):

        A = [[1, 2, 3],
            [5, 6, 7], 
            [4, 6, 8]]
        
        B = [[1, 2, 3],
            [5, 6, 7], 
            [4, 6, 8]]

        C = list.copy(A)

        result = verify_matrix_multiplication(A, B, C)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()


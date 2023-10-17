import unittest
from ex3_4 import Field

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


if __name__ == '__main__':
    unittest.main()




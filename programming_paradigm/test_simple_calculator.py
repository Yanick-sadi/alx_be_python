import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.addition(2, 3), 5)
        self.assertEqual(self.calc.addition(-1, 1), 0)
        self.assertEqual(self.calc.addition(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtraction(5, 3), 2)
        self.assertEqual(self.calc.subtraction(0, 5), -5)
        self.assertEqual(self.calc.subtraction(-3, -2), -1)


    def test_multiplication(self):
        self.assertEqual(self.calc.multiplication(4, 3), 12)
        self.assertEqual(self.calc.multiplication(-2, 3), -6)
        self.assertEqual(self.calc.multiplication(0, 5), 0)

    def test_division(self):
        self.assertEqual(self.calc.divisi(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(0, 5), 0)

if __name__ == '__main__':
    unittest.main()
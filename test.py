import unittest
import fractions
import random


from Myapp import (
    random_fraction,
    random_expression,
    is_valid,
    evaluate,
    generate_expressions,
)


class TestMathExpressions(unittest.TestCase):

    def test_random_fraction(self):
        max_denominator = 10
        frac = random_fraction(max_denominator)
        self.assertTrue(0 <= frac.numerator < max_denominator)
        self.assertTrue(1 <= frac.denominator <= max_denominator)

    def test_random_expression(self):
        max_denominator = 10
        expression = random_expression(max_denominator, 3)
        self.assertIsInstance(expression, str)

    def test_is_valid(self):
        valid_expression = "1/2 + 1/3"
        invalid_expression = "1/2 - 3/4"
        self.assertTrue(is_valid(valid_expression))
        self.assertFalse(is_valid(invalid_expression))

    def test_evaluate(self):
        expression = "1/2 + 1/3"
        expected_result = fractions.Fraction(5, 6)
        self.assertEqual(evaluate(expression), expected_result)

    def test_generate_expressions(self):
        n = 5
        max_denominator = 10
        expressions = generate_expressions(n, max_denominator)
        self.assertEqual(len(expressions), n)


if __name__ == '__main__':
    unittest.main()



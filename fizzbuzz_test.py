import unittest
from fizzbuzz import fizz_buzz


class test_fb(unittest.TestCase):

    def test_default_case(self):
        self.assertEqual(fizz_buzz(1), '1')

    def test_fizz(self):
        self.assertEqual(fizz_buzz(6), 'Fizz')

    def test_buzz(self):
        self.assertEqual(fizz_buzz(10), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(fizz_buzz(30), 'FizzBuzz')

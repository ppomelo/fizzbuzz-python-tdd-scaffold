import unittest
from fizzbuzz import FizzBuzz

class test_fb(unittest.TestCase):

    def test_default_case(self):
        self.assertEqual(FizzBuzz(1), '1')

    def test_fizz(self):
        self.assertEqual(FizzBuzz(6), 'Fizz')
    
    def test_buzz(self):
        self.assertEqual(FizzBuzz(10), 'Buzz')

    def test_fizzbuzz(self):
        self.assertEqual(FizzBuzz(30), 'FizzBuzz')
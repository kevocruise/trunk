"""
Calculator class able to perform many functions, and includes
unittesting and doctest coverage.
"""


class Calculator:
    """Calculator class acts as a real calculator"""

    def _addition(first_number, second_number):
        """Addition function returns the sum

        Given two numbers, return the sum of the two numbers.

        Arguments:
        first_number - the first number
        second_number - the second number

        >>> Calculator._addition(1, 2)
        3

        """ 
       
        try:
            return int(first_number) +  int(second_number)
       
        except:
            raise ValueError("cannot add those two arguments together")


    def _subtraction(first_number, second_number):
        """Subtraction function returns difference
 
        Given a first number and second number, return the difference between
        the first to the second

        Arguments:
        first_number - the first number
        second_number - the second number

        >>> Calculator._subtraction(5, 3)
        2

        """
 
        try:
            return int(first_number) - int(second_number)
 
        except:
            raise ValueError("cannot subtract the second argument from the first")

####################################################################################
"""
unittest demo against calculator class

command-line examples:
python3.2 -m unittest calculator
python3.2 -m unittest calculator.CalculatorTestCase
python3.2 -m unittest calculator.CalculatorTestCase.test_addition
"""

import unittest
class CalculatorTestCase(unittest.TestCase):

    def setUp(self):
        self.__calc = Calculator


    def test_addition(self):
        """Test addition function of calculator"""
        self.assertEqual(47, self.__calc._addition(34,13))
        self.assertRaises(ValueError, self.__calc._addition, "hello", 4)

    def test_subtraction(self):
        """Test subtraction function of calculator"""
        self.assertEqual(23, self.__calc._subtraction(54, 31))
        self.assertRaises(ValueError, self.__calc._subtraction, "hello", 5)

####################################################################################
"""
doctest demo against calculator class - runs test in function docstrings

command-line examples:
python3.2 -m doctest calculator.py
python3.2 -m doctest -v calculator.py

"""

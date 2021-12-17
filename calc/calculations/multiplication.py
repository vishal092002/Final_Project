"""Class For The Multiplication Opperation """
from calc.calculations.calculation import Calculation

class Multiplication(Calculation):
    """subtraction calculation object"""
    def get_result(self):
        """gets the result after the two numbers are multiplied"""
        result = 1.0
        for value in self.values:
            result = result * value
        return result

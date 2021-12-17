"""Addition Opperation Class"""
from calc.calculations.calculation import Calculation

class Addition(Calculation):
    """ Class for the additon opperation"""
    def get_result(self):
        """gets the result after adding the two numbers """
        sum_of_values = 0.0
        for value in self.values:
            sum_of_values = value + sum_of_values
        return sum_of_values

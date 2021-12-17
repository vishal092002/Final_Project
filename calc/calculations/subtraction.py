"""Class For Subtraction Opperation"""
import pprint

from calc.calculations.calculation import Calculation

class Subtraction(Calculation):
    def get_result(self):
        """get the result after the two numbers are subtracted"""
        difference_of_values = 0.0
        for value in self.values:
            difference_of_values =   difference_of_values - value
            pprint.pprint(value)
        return difference_of_values

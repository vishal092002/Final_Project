"""Testing Subtraction Operation"""
from calc.calculations.subtraction import Subtraction

def test_calculation_subtraction():
    #Arrange
    mynumbers = (1.0,2.0)
    subtraction = Subtraction(mynumbers)
    #Act
    #Assert
    assert subtraction.get_result() == -3

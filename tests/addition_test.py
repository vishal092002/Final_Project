"""Testing Addition Operation"""
from calc.calculations.addition import Addition

def test_calculation_addition():
    #Arrange
    mynumbers = (1.0,2.0)
    addition = Addition(mynumbers)
    #Act
    #Assert
    assert addition.get_result() == 3.0

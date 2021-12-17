"""Testing the Calculator"""
import pytest
from calc.calculator import Calculator
from calc.history.calculations import Calculations
@pytest.fixture
def clear_history_fixture():


    Calculations.clear_history()
def test_calculator_add_static(clear_history_fixture):

    my_tuple = (1.0,2.0,5.0)
    Calculator.addition(my_tuple)
    assert Calculator.get_last_result_value() == 8.0
def test_calculator_subtract_static(clear_history_fixture):
    my_tuple = (1.0,2.0,3.0)
    Calculator.subtraction(my_tuple)
    assert Calculator.get_last_result_value() == -6.0

def test_calculator_multiply_static(clear_history_fixture):
    my_tuple = (1.0,2.0,3.0)
    Calculator.multiplication(my_tuple)
    assert Calculator.get_last_result_value() == 6.0

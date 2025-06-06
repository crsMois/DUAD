import pytest
from week6_Exercise_6 import sort_string_elements


def test_sort_string_elements():

    # Arrange
    
    input_string = "python-variable-funcion-computadora-monitor"

    # Act
    result = sort_string_elements(input_string)
    
    # Assert
    assert result == "computadora-funcion-monitor-python-variable"



def test_return_at_least_1_hyphen():

    # Arrange
    
    input_string = "computadora?funcion?monitor?python?variable"

    # Act
    with pytest.raises(ValueError):
        result = sort_string_elements(input_string)
    
    # Assert



def test_if_iterable():
    # Arrange
    
    input_string = 88

    # Act
    with pytest.raises(TypeError):
        result = sort_string_elements(input_string)








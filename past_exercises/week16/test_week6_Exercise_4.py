import pytest
from week6_Exercise_4 import return_ordered_string


def test_return_ordered_string():

    # Arrange
    
    input_string = "Hola mundo"

    # Act
    result = return_ordered_string(input_string)
    
    # Assert
    assert result == "odnum aloH"



def test_at_leat_1_value_in_string():
    # Arrange
    
    input_string = ""

    # Act
    with pytest.raises(ValueError):
        result = return_ordered_string(input_string)




def test_if_not_string_value_input():
    # Arrange
    
    input_string = 77.7

    # Act
    with pytest.raises(AttributeError):
        result = return_ordered_string(input_string)








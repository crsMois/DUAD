import pytest
from week6_Exercise_5 import get_upper_lower_case_from_string


def test_return_upper_case_characters():

    # Arrange
    
    input_string = "I love Nación Sushi"

    # Act
    result = get_upper_lower_case_from_string(input_string)
    
    # Assert
    assert result[0] == 3



def test_return_lower_case_characters():

    # Arrange
    
    input_string = "I love Nación Sushi"

    # Act
    result = get_upper_lower_case_from_string(input_string)
    
    # Assert
    assert result[1] == 13



def test_if_not_string_input():
    # Arrange
    
    input_string = 88

    # Act
    with pytest.raises(TypeError):
        result = get_upper_lower_case_from_string(input_string)








import pytest
from week6_Exercise_3 import sum_list


def test_sum_list():

    # Arrange
    
    input_list = [1,4,7]

    # Act
    result = sum_list(input_list)
    
    # Assert
    assert result == 12



def test_if_not_number_in_list():
    # Arrange
    
    input_list = [0,1,"f",6]

    # Act
    with pytest.raises(TypeError):
        result = sum_list(input_list)



def test_list_if_not_list():
    # Arrange
    
    input_list = "This is not a list"

    # Act
    with pytest.raises(TypeError):
        result = sum_list(input_list)








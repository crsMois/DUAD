import pytest
from week6_Exercise_7 import create_list_prime_numbers,validate_if_prime


def test_create_list_prime_numbers():

    # Arrange
    
    numbers_list = [1, 4, 6, 7, 13, 9, 67]

    # Act
    result = create_list_prime_numbers(numbers_list)
    
    # Assert
    assert result == [7, 13, 67]


def test_if_is_not_list_or_has_less_2_values():
    # Arrange
    
    numbers_list = [1]

    # Act
    with pytest.raises(ValueError):
        result = create_list_prime_numbers(numbers_list)



def test_validate_if_prime_if_list_has_numbers():

    # Arrange
    
    numbers_list = [1, 4, 6, 7, 13, 9, "pytest"]

    # Act
    with pytest.raises(TypeError):
        result = validate_if_prime(numbers_list)
    
    # Assert











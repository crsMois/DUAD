import pytest
from BubbleSort import BubbleSortList



def test_sort_list_short_list():
    # Arrange

    input_list = [5, 6, 2, 8, 7, 5, 5, 6, 2, 7]

    # Act
    sortBubbleList = BubbleSortList(input_list)
    result = BubbleSortList.sort_list(sortBubbleList)
    
    # Assert
    assert len(result) < 100



def test_sort_list_big_list():

    # Arrange
    
    input_list = [
    5, 6, 2, 8, 7, 5, 5, 6, 2, 7,
    8, 8, 5, 2, 6, 7, 5, 2, 8, 6,
    7, 5, 6, 2, 8, 7, 5, 5, 8, 2,
    6, 7, 6, 2, 5, 8, 7, 5, 6, 2,
    7, 8, 5, 5, 6, 2, 7, 8, 6, 5,
    2, 7, 8, 5, 6, 2, 7, 5, 8, 6,
    2, 7, 5, 8, 6, 2, 7, 5, 6, 8,
    2, 7, 5, 8, 6, 2, 7, 5, 6, 2,
    8, 7, 5, 5, 6, 2, 8, 7, 6, 5,
    2, 8, 7, 5, 6, 2, 7, 5, 8, 6,
    2, 7, 5, 6, 8, 2, 7
]

    # Act
    sortBubbleList = BubbleSortList(input_list)
    result = BubbleSortList.sort_list(sortBubbleList)

    # Assert
    assert len(result) >= 100



def test_sort_list_empty_list():
    # Arrange
    
    input_list = []

    # Act
    sortBubbleList = BubbleSortList(input_list)
    result = BubbleSortList.sort_list(sortBubbleList)

    # Assert
    assert result == []



def test_sort_list_if_not_list():
    # Arrange
    
    input_list = "This is not a list"

    # Act
    with pytest.raises(TypeError):
        sortBubbleList = BubbleSortList(input_list)
        result = BubbleSortList.sort_list(sortBubbleList)






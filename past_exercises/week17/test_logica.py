import pytest
from Logic import read_source_movements_file, validate_if_category_exists
from Persistence import read_categories_file,write_movement_file, open_source_movements_csv



def test_if_category_file_exists_fail():

    # Arrange
    src_file =  "categori.csv"

    # Act
    
    with pytest.raises(FileNotFoundError):
        categories=list(read_categories_file(src_file))
        result = validate_if_category_exists(src_file,categories)
    
    # Assert


def test_if_choose_category_exist_success():

    # Arrange
    src_file =  "categories.csv"
    chosen_category = "Bussiness"

    # Act

    categories=list(read_categories_file(src_file))
    result = validate_if_category_exists(chosen_category,categories)
    
    # Assert
    assert result == True


def test_if_choose_category_exist_false():

    # Arrange
    src_file =  "categories.csv"
    chosen_category = "English"

    # Act[]

    categories=list(read_categories_file(src_file))
    result = validate_if_category_exists(chosen_category,categories)
    
    # Assert
    assert result == False



def test_open_source_movements_csv():

    # Arrange
    movement_file = "movements.csv"

    # Act[]
    open_source_movements_csv(movement_file)

    # Assert


def test_write_movement_file_list_not_complete_fail():

    # Arrange
    movement_list=["Gym",1000,"category"]

    # Act
    with pytest.raises(IndexError):
        write = write_movement_file("movements.csv",movement_list)
        assert write == True  
    # Assert


def test_write_movement_file_list_complete_success():

    # Arrange
    movement_list=["Gym",1000,"category","expense"]

    # Act
    write = write_movement_file("movements.csv",movement_list)
    assert write == True  
    # Assert



def test_read_source_movements_file_return_list():

    #Arrange    
    movement_file= "movements.csv"

    #Act 
    file_output = read_source_movements_file(movement_file)

    #Assert
    assert isinstance(file_output, list)



def test_read_source_movements_file_return_list_failed():

    #Arrange    
    movement_file= "movemes.csv"

    #Act 
    with pytest.raises(IndexError):
        file_output = read_source_movements_file(movement_file)
    #Assert

    
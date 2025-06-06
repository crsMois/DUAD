	
my_string= "Hola mundo"

def return_ordered_string(new_string):

    if not new_string or new_string.strip() == "":
        raise ValueError("The string must contain at least one non-empty character")
    
    my_ordered_string=""
    for value in range (0,len(new_string)):
        my_ordered_string = my_ordered_string + str(new_string[len(new_string)-value-1])
        

    return my_ordered_string


print(return_ordered_string(my_string))
my_string="python-variable-funcion-computadora-monitor"

def sort_string_elements(new_string):
    
    if "-" not in new_string:
        raise ValueError("The string must contain at least one hyphen '-'")

    my_string_list = new_string.split("-")
    my_string_list.sort()
    new_string= "-".join(my_string_list)

    return new_string


print(sort_string_elements(my_string))  
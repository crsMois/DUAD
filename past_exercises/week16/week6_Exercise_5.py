my_string="I love Nación Sushi"

def get_upper_lower_case_from_string(new_string):
    
    upper_case_characters= 0
    lower_case_characters= 0
    list = [0,0]

    for character in new_string:
        if (character.isupper()):
            upper_case_characters=upper_case_characters+ 1
        elif(character.islower()):
            lower_case_characters=lower_case_characters+ 1
    
    list[0]=upper_case_characters
    list[1]=lower_case_characters

    return list

characters= get_upper_lower_case_from_string(my_string)
print((f"There’s {characters[0]} upper cases and {characters[1]} lower cases"))
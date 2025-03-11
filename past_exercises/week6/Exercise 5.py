my_string="I love Nación Sushi"

def get_upper_lower_case_from_string(new_string):
    
    upper_case_characters= 0
    lower_case_characters= 0

    for character in new_string:
        if (character.isupper()):
            upper_case_characters=upper_case_characters+ 1
        elif(character.islower()):
            lower_case_characters=lower_case_characters+ 1
    return (f"There’s {upper_case_characters} upper cases and {lower_case_characters} lower cases")

print(get_upper_lower_case_from_string(my_string))
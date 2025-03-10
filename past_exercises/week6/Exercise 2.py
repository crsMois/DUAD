current_year= 2027 


def get_your_age():
    born_year = 2015
    current_year=2025
    print(f"(INSIDE FUNCTION) you current age is {(current_year-born_year)}")

get_your_age()

print(f"(OUTSIDE FUNCTION) you current age is {(current_year-born_year)}")
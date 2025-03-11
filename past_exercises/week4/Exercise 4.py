user_number= 0
highest_number = 0

for i in range(3):
 user_number= int(input((f"Please enter the number{i+1} ")))
 if (user_number > highest_number):
    highest_number = user_number


print(f"The highest numer is  {highest_number}")
total_amount_grades_input = 5
approved_grades_counter = 0
failed_grades_counter = 0
approved_grades_total = 0
failed_grades_total = 0
user_grade = 0
approved_average= 0
failed_average= 0
total_average = 0



for i in range(total_amount_grades_input):
    user_grade=int(input(f"Please enter the grade{i}: "))
    if (user_grade<70):
        failed_grades_counter = failed_grades_counter + 1
        failed_grades_total = failed_grades_total+user_grade
    else:
        approved_grades_counter = approved_grades_counter + 1    
        approved_grades_total = approved_grades_total+user_grade


try:
    total_average = (approved_grades_total+failed_grades_total)/total_amount_grades_input
except ZeroDivisionError:
    total_average = 0

try:
    approved_average = approved_grades_total/approved_grades_counter
except ZeroDivisionError:
    approved_average = 0

try:
    failed_average = failed_grades_total/failed_grades_counter
except ZeroDivisionError:
    failed_average = 0



print (f"Passed grades greater than or equal to 70: {approved_grades_counter} ")
print (f"Failed grades less than 70: {failed_grades_counter} ")
print (f"Total grade point average (including passed and failed grades): {total_average} ")
print (f"Approved average greater than or equal to 70: {approved_average} ")
print (f"Failed average less than 70: {failed_average} ")
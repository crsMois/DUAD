from actions import add_new_student, get_top_3_students, get_group_average_grade , get_all_students, export_students_list_to_file
from data import open_source_students_csv

def menu_prompt(dict_list_on_memory):

    print("\n\n1. Enter a New Student")
    print("2. View information on all enrolled students")
    print("3. Show Top 3 students")
    print("4. Show the group's overall average grade")
    print("5. Export list to CSV \n\n")
    print("6. Salir\n\n")

    source_csv = "Student.csv"
    client_option=input (f"\n Select one of the options from the list above:  ")
    
    try:
        user_chosen_menu_option(client_option,dict_list_on_memory,source_csv)
    except Exception as error:
            print(f"Please enter an correct menu value, a Number between 1-5 {error}...")
            menu_prompt(dict_list_on_memory)



def user_chosen_menu_option(user_option,source_csv_file_list,source_csv):
    user_option=int(user_option)
    
    if(user_option==1):
        updated_list=add_new_student(source_csv)
        menu_prompt(updated_list)

    if(user_option==2):

#THIS OPTION CALLS THE GET_ALL_STUDENTS() FUNCTION IN ACTION.PY , 
#DONT WANT TO PUT THE PRINT FORMAT IN THAT FUNCTION BUT JUST THE LIST RETURNED WITH THE RAW DATA AND WE FORMAT HERE

        list_all_students=get_all_students(source_csv_file_list)

        print ('-' * 30 +" All Students " + '-' * 30)
        Counter=0

        for item in list_all_students:
            Counter= Counter + 1
            print(str(Counter)+ ")")
            print(f"Name: {item['name']}")
            print(f"Section: {item['section']}")
            print(f"Spanish: {item['spanish']}")
            print(f"English: {item['english']}")
            print(f"Social: {item['social']}")
            print(f"Science: {item['science']}")
            print(f"Average Grade: {item['average']} *")
            print('-' * 30) 
        menu_prompt(source_csv_file_list)


    if(user_option==3):
#THIS OPTION CALLS THE GET_TOP_3_STUDENTS() FUNCTION IN ACTION.PY , 
#DONT WANT TO PUT THE PRINT FORMAT IN THAT FUNCTION BUT JUST THE LIST RETURNED WITH THE RAW DATA AND WE FORMAT HERE


        list_of_top_students=(get_top_3_students(source_csv_file_list))
        print ('-' * 30 +" TOP 3 Students " + '-' * 30)
        Counter=0

        for item in list_of_top_students:
            Counter= Counter + 1
            print(str(Counter)+ ")")
            print(f"Name: {item['name']}")
            print(f"Section: {item['section']}")
            print(f"Spanish: {item['spanish']}")
            print(f"English: {item['english']}")
            print(f"Social: {item['social']}")
            print(f"Science: {item['science']}")
            print(f"Average Grade: {item['average']} *")
            print('-' * 30) 
        menu_prompt(source_csv_file_list)

#THIS OPTION CALLS THE GET_GROUP_AVERAGE_GRADE() FUNCTION IN ACTION.PY , 
#DONT WANT TO PUT THE PRINT FORMAT IN THAT FUNCTION BUT JUST THE LIST RETURNED WITH THE RAW DATA AND WE FORMAT HERE

    if(user_option==4):
        print(f"\n\n The group's overall average grade is: [{get_group_average_grade(source_csv_file_list)}]")
        menu_prompt(source_csv_file_list)


    if(user_option==5):
        export_students_list_to_file(source_csv,source_csv_file_list)
        menu_prompt(source_csv_file_list)


    if(user_option==6):
        exit()
        menu_prompt(source_csv_file_list)

    print(f"Please enter an correct menu value, a Number between 1-5 ...")
    menu_prompt(source_csv_file_list)



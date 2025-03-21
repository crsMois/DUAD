from actions import add_new_student, get_top_3_students, get_group_average_grade , get_all_students
from data import open_source_students_csv

def menu_prompt():

    print("\n\n1. Enter a New Student")
    print("2. View information on all enrolled students")
    print("3. Show Top 3 students")
    print("4. Show the group's overall average grade")
    print("5. Salir\n\n")

    source_csv = "Student.csv"
    client_option=input (f"\n Select one of the options from the list above:  ")
    
    try:
        user_chosen_menu_option(client_option,source_csv)
    except Exception as error:
            print(f"Please enter an correct menu value, a Number between 1-5 {error}...")
            menu_prompt()



def user_chosen_menu_option(user_option,source_csv):
    user_option=int(user_option)
    source_csv_file=open_source_students_csv(source_csv)
    
    if(user_option==1):
        add_new_student(source_csv)
        menu_prompt()

    if(user_option==2):

#THIS OPTION CALLS THE GET_ALL_STUDENTS() FUNCTION IN ACTION.PY , 
#DONT WANT TO PUT THE PRINT FORMAT IN THAT FUNCTION BUT JUST THE LIST RETURNED WITH THE RAW DATA AND WE FORMAT HERE

        list_all_students=get_all_students(source_csv_file)

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
        menu_prompt()


    if(user_option==3):
#THIS OPTION CALLS THE GET_TOP_3_STUDENTS() FUNCTION IN ACTION.PY , 
#DONT WANT TO PUT THE PRINT FORMAT IN THAT FUNCTION BUT JUST THE LIST RETURNED WITH THE RAW DATA AND WE FORMAT HERE


        list_of_top_students=(get_top_3_students(source_csv_file))
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
        menu_prompt()

#THIS OPTION CALLS THE GET_GROUP_AVERAGE_GRADE() FUNCTION IN ACTION.PY , 
#DONT WANT TO PUT THE PRINT FORMAT IN THAT FUNCTION BUT JUST THE LIST RETURNED WITH THE RAW DATA AND WE FORMAT HERE

    if(user_option==4):
        print(f"\n\n The group's overall average grade is: [{get_group_average_grade(source_csv_file)}]")
        menu_prompt()


    if(user_option==5):
        exit()
        menu_prompt()


    print(f"Please enter an correct menu value, a Number between 1-5 ...")
    menu_prompt()



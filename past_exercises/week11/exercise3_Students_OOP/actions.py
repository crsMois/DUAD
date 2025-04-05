from Students import Students
import csv
from data import open_source_students_csv, write_student_file

def add_new_student(source_students_csv,source_students_list):
        
    name = 0
    section= 0
    spanish= 0
    english= 0
    social= 0
    science= 0
    average=0



    while True:
        try:
            name= input("Enter the Student Name: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")

    while True:
        try:
            section= input("Enter the Student Section: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")

# FORCING TO USE RANGE 0 - 100 FOR THE GRADES 

    while True:

        
        try:
            spanish= float(input("Enter the Spanish Grade: "))
            if (spanish < 1 or spanish > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")
            

    while True:
        try:
            english= float(input("Enter English Grade: "))
            if (english < 1 or english  > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")   
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")


    while True:
        try:
            social= float(input("Enter Social Studies Grade: "))
            if (social < 1 or social > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")   
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")


    while True:
        try:
            science= float(input("Enter Science Grade: "))
            if (science < 1 or science  > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")   
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")


# CALCULATING THE AVERAGE AT ONCE AND MAKING PERSISTENT(SENDING IT TO FILE) TO OPTIMIZE MEMORY AND CPU UTILIZATION

    average = float((spanish+ english + social + science)/4)
    student = Students(name,section,spanish,english,social,science,average)

    source_students_list.append(student)

#WRITING THE FILE (DATA FUNCTION) TO THE CSV FILE AND THE NEW LIST WITH THE NEW ELEMENT (DICTIONARY)

    return source_students_list


def export_students_list_to_file(source_students_csv,source_memory_object_list):

    students_dict_list = []
    
    for object_student in source_memory_object_list:

# I CREATE A NEW INSTANCE OF THE DICT EACH TIME TO NOT POINT TO THE SAME DICT EVERY TIME

        dict_new_student =   {
		'name': '',
		'section': '',
		'spanish': 0,
		'english': 0,
        'social': 0,
        'science': 0,
        'average': 0,
        }  
    
        dict_new_student["name"]= object_student.name
        dict_new_student["section"]= object_student.section
        dict_new_student["spanish"]= object_student.spanish
        dict_new_student["english"]= object_student.english
        dict_new_student["social"]= object_student.social
        dict_new_student["science"]= object_student.science
        dict_new_student["average"]= object_student.avg_grade
        students_dict_list.append(dict_new_student)


    write_student_file(source_students_csv,students_dict_list) 


def import_students_from_csv_file(source_csv):
    
    source_csv_file_list=open_source_students_csv(source_csv)
    dict_to_object_list= []

    for item in source_csv_file_list:
        student= Students(item['name'],item['section'],float(item['spanish']),float(item['english']),float(item['social']),float(item['science']),float(item['average'])) 
        dict_to_object_list.append(student)
        
    print("\n\n List of students has been imported to the system!!!! \n\n")
    return dict_to_object_list


def get_top_3_students(source_students_list):

    ordered_student_list=sorted(source_students_list, key=lambda persona: persona.avg_grade, reverse=True)

    top_3_students_list = []

    try:
        top_3_students_list.append(ordered_student_list[0])
    except IndexError:
        print("\n\n The list is empty, need to add new students \n\n")
    
    try:
        top_3_students_list.append(ordered_student_list[1])
    except IndexError:
        if (len(top_3_students_list)==1):
            print("The list just have 1 Student added")

    try:
        top_3_students_list.append(ordered_student_list[2])
    except IndexError:
        if (len(top_3_students_list)==2):
            print("The list just have 2 Students added")
        


    return top_3_students_list


def get_all_students(source_students_list):
        
        return source_students_list


def get_group_average_grade(source_students_list):
    
    sum_of_avg= 0

    for item in source_students_list:
        sum_of_avg= sum_of_avg+float(item.avg_grade)
    try:
        total_avg=sum_of_avg/len(source_students_list)
    except ZeroDivisionError:
        print("\n\n There is no Students in the list , no average group grade to calculate")
        total_avg=0
    
    
    return total_avg
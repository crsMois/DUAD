import csv
from data import open_source_students_csv, write_student_file

def add_new_student(source_students_csv):
        
    dict_new_student =   {
		'name': '',
		'section': '',
		'spanish': 0,
		'english': 0,
        'social': 0,
        'science': 0,
        'average': 0,
        }  



    while True:
        try:
            dict_new_student["name"]= input("Enter the Student Name: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")

    while True:
        try:
            dict_new_student["section"]= input("Enter the Student Section: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")



# FORCING TO USE RANGE 0 - 100 FOR THE GRADES 

    while True:

        
        try:
            dict_new_student["spanish"]= float(input("Enter the Spanish Grade: "))
            if (dict_new_student["spanish"] < 1 or dict_new_student["spanish"]  > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")
            

    while True:
        try:
            dict_new_student["english"]= float(input("Enter English Grade: "))
            if (dict_new_student["english"] < 1 or dict_new_student["spanish"]  > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")   
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")


    while True:
        try:
            dict_new_student["social"]= float(input("Enter Social Studies Grade: "))
            if (dict_new_student["social"] < 1 or dict_new_student["social"]  > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")   
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")


    while True:
        try:
            dict_new_student["science"]= float(input("Enter Science Grade: "))
            if (dict_new_student["science"] < 1 or dict_new_student["science"]  > 100):
                raise ValueError()
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")   
        except ValueError as error:
            print(f"Please enter a value between 0 and 100{error}...")


# CALCULATING THE AVERAGE AT ONCE AND MAKING PERSISTENT(SENDING IT TO FILE) TO OPTIMIZE MEMORY AND CPU UTILIZATION

    dict_new_student["average"] = float((dict_new_student["spanish"] + dict_new_student["english"] + dict_new_student["social"] + dict_new_student["science"])/4)

    converted_source_list=list(open_source_students_csv(source_students_csv))
    converted_source_list.append(dict_new_student)

#WRITING THE FILE (DATA FUNCTION) TO THE CSV FILE AND THE NEW LIST WITH THE NEW ELEMENT (DICTIONARY)

    write_student_file(source_students_csv,converted_source_list) 

    return converted_source_list




def get_top_3_students(source_students_list):

#FORCING THE AVERAGE GRADE FOR EACH STUDENT TO FLOAT , SO WE HAVE A RIGHT SORTED BY AVERAGE USING FLOAT INSTEAD STRING


    for student in source_students_list:
        student['average'] = float(student['average'])
    
    ordered_student_list=sorted(source_students_list, key=lambda x: x['average'], reverse=True)
    top_3_students_list = []

    top_3_students_list.append(ordered_student_list[0])
    top_3_students_list.append(ordered_student_list[1])
    top_3_students_list.append(ordered_student_list[2])

    return top_3_students_list


def get_all_students(source_students_list):
        
#FORCING THE AVERAGE GRADE FOR EACH STUDENT TO FLOAT , SO WE HAVE A RIGHT SORTED BY AVERAGE USING FLOAT INSTEAD STRING

        for student in source_students_list:
            student['average'] = float(student['average'])

        source_students_list=sorted(source_students_list, key=lambda x: x['average'], reverse=True)
        
        return source_students_list


def get_group_average_grade(source_students_list):
    
    sum_of_avg= 0

    for item in source_students_list:
        sum_of_avg= sum_of_avg+float(item["average"])

    total_avg=sum_of_avg/len(source_students_list)

    return total_avg
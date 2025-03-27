import csv

def open_source_students_csv(source_students_csv):
    
    list_students_py = []
    try:
        with open(source_students_csv,"r") as student_read_file:
            list_students_py=list(csv.DictReader(student_read_file))
            
    except FileNotFoundError as error:    
            print(f"\n\n\n The Student FILE does not exist, creating a new empty FILE !!!!!! \n\n\n")
            write_student_file(source_students_csv,list_students_py)
            open_source_students_csv(source_students_csv)

    return list_students_py



def write_student_file(in_file_to_create, data_list):

    students_dict = {
		'name': '',
		'section': '',
		'spanish': '',
		'english': '',
        'social': '',
        'science': '',
        'average': '',
	}


#USING THE DICT HEADERS KEYS IN WRITEHEADER FUNCTION

    with open(in_file_to_create,"w", newline='') as file:
        writer = csv.DictWriter(file, students_dict.keys())
        writer.writeheader()
        writer.writerows(data_list)
        print("Succesfully exported to Students CSV file")

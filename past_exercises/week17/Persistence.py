import csv

def open_source_movements_csv(source_movement_csv):
    
    list_movements_py = []
    try:
        with open(source_movement_csv,"r") as movement_read_file:
            list_movements_py=list(csv.DictReader(movement_read_file))
            
    except FileNotFoundError as error:    
            print(f"\n\n\n The Movement FILE does not exist, creating a new empty FILE !!!!!! \n\n\n")
            write_movement_file(source_movement_csv,list_movements_py)
            open_source_movements_csv(source_movement_csv)

    return list_movements_py



def write_movement_file(src_file, movement_list):

    write = False

    movement_dict_list=[]
    movement_dict = {
	}

    movement_dict["Name"] = movement_list[0]
    movement_dict["Amount"] = movement_list[1]
    movement_dict["Category"] = movement_list[2]
    movement_dict["Type"] = movement_list[3]

    movement_dict_list.append(movement_dict)

    with open(src_file,"a", newline='') as file:
        writer = csv.DictWriter(file, movement_dict.keys())
        writer.writerows(movement_dict_list)
        print("Successfully exported to Movement CSV file")
        write = True
        return write


def read_categories_file(csv_category_file):

    lines = []
    with open(csv_category_file, 'r', encoding='utf-8') as file:
        for line in file:
            lines.append(line.strip())
    return lines



def write_category_file(newfile, new_category):

    csv_line = new_category

    # Open the CSV file in append mode ('a')
    with open(newfile, 'a', newline='') as file:
        file.write(csv_line + '\n') 

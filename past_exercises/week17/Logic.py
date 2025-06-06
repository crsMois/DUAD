from Persistence import open_source_movements_csv 


def read_source_movements_file(csv_mov_file):
    headings = ["Name","Amount","Category","Type"]
    movement_list = open_source_movements_csv(csv_mov_file)
    rows = [[d.get(col, '') for col in headings] for d in movement_list]
    return rows



def validate_if_category_exists(value, category_list):
    exist=False

    for item in category_list:
        if(value==item):
            exist=True

    return exist

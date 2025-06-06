import FreeSimpleGUI as sg
from Persistence import write_category_file,write_movement_file,read_categories_file,open_source_movements_csv
from Logic import validate_if_category_exists,read_source_movements_file


def show_add_category_window(csv_category_file, finance_manager):

    layout = [
        [sg.Text("Category", key="cat_key")],
        [sg.Input(key="cat_input_key")],
        [sg.Column([
            [sg.Button("Save"), sg.Button("Cancel")]
        ], element_justification='center')],
    ]

    window = sg.Window("Add Category", layout)
    category = finance_manager.category

    while True:
        event, values = window.read()
    
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Save" and values["cat_input_key"]: 
            category.category_name = values["cat_input_key"]
            write_category_file(csv_category_file,category.category_name)
            print("category saved")
            sg.popup(f"Category '{category.category_name}' has been added successfully!", title="Success", keep_on_top=True)
        
            window.close()
        if not values["cat_input_key"]:
                        sg.popup_error("Please enter a category name.", title="Input Error")

    window.close()



def show_add_income_window(csv_mov_file,csv_category_file,finance_manager):
    
    categories=list(read_categories_file(csv_category_file))
    finance_manager.movement.type="Income"
    income = finance_manager.movement

    layout = [
        [sg.Column([
            [sg.Text("Income"), sg.Input(key="income_name_key")]
        ], element_justification='center')],
    
        [sg.Column([
            [sg.Text("Amount"), sg.Input(key="income_amount_key")]
        ], element_justification='center')],

        [sg.Column([
            [sg.Text("Category"), sg.Combo(categories, default_value=categories[0], key="category_combo_key", enable_events=True)]
        ], element_justification='center')],

        [sg.Column([
            [sg.Button("Save"), sg.Button("Cancel")]
        ], element_justification='center')],
    ]
    window = sg.Window("Add Income", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        if event == "Save" and  values["income_name_key"] and values["income_amount_key"] and values["category_combo_key"] :
            
            income.name = values["income_name_key"]

        # Income value must be a number
            try:
                income.category = values["category_combo_key"]
                income.amount = float(values["income_amount_key"])
                movement_list=[income.name,income.amount,income.category,income.type]
        
        #Just if exist it will write the new Category
                if (validate_if_category_exists(income.category, categories) == True):

                    write_movement_file(csv_mov_file,movement_list)
                    sg.popup(f"Income '{income.name}' has been added successfully!", title="Success", keep_on_top=True)
                    
                    window.close()
                else:
                    sg.popup_error("That Category does not exist , please select from the list", title="Input Error")

            except ValueError as error:
                sg.popup_error("Please enter a number for amount field.", title="Input Error")

        if not values["income_name_key"] or not values["income_amount_key"] or not values["category_combo_key"] :
            sg.popup_error("Please enter all Income values.", title="Input Error")

    window.close()





def show_add_expense_window(csv_mov_file,csv_category_file,finance_manager):
    
    categories=list(read_categories_file(csv_category_file))
    finance_manager.movement.type="Expense"
    expense = finance_manager.movement

    layout = [
        [sg.Column([
            [sg.Text("Expense"), sg.Input(key="expense_name_key")]
        ], element_justification='center')],
    
        [sg.Column([
            [sg.Text("Amount "), sg.Input(key="expense_amount_key")]
        ], element_justification='center')],

        [sg.Column([
            [sg.Text("Category"), sg.Combo(categories, default_value=categories[0], key="category_combo_key", enable_events=True)]
        ], element_justification='center')],

        [sg.Column([
            [sg.Button("Save"), sg.Button("Cancel")]
        ], element_justification='center')],
    ]

    window = sg.Window("Add Expense", layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == "Cancel":
            break

        if event == "Save" and  values["expense_name_key"] and values["expense_amount_key"] and values["category_combo_key"] :
            
            expense.name = values["expense_name_key"]

        # Income value must be a number
            try:
                expense.category = values["category_combo_key"]
                expense.amount = float(values["expense_amount_key"])
                movement_list=[expense.name,expense.amount,expense.category,expense.type]

                if (validate_if_category_exists(expense.category, categories) == True):

                    write_movement_file(csv_mov_file,movement_list)
                    sg.popup(f"Expense '{expense.name}' has been added successfully!", title="Success", keep_on_top=True)
                    
                    window.close()
                else:
                    sg.popup_error("That Category does not exist , please select from the list", title="Input Error")

            except ValueError as error:
                sg.popup_error("Please enter a number for amount field.", title="Input Error")

        if not values["expense_name_key"] or not values["expense_amount_key"] or not values["category_combo_key"] :
            sg.popup_error("Please enter all Income values.", title="Input Error")

    window.close()





def show_main_window(csv_mov_file, csv_category_file, finance_manager):

    headings = ["Name","Amount","Category","Type"]
    movement_list = open_source_movements_csv(csv_mov_file)
    rows = [[d.get(col, '') for col in headings] for d in movement_list]

    layout = [
        [sg.Column([
            [sg.Table(values=rows, headings=["Name", "Amount", "Category","Type"],
                key="table", enable_events=True, select_mode=sg.TABLE_SELECT_MODE_BROWSE,col_widths=[40, 50, 50],cols_justification='c'), sg.Button("Add Category")]
        ], element_justification='center')],
        [sg.Text("", key="output")],
        [sg.Column([
            [sg.Button("Add Income"), sg.Button("Add Expense")]
        ], element_justification='center')]
    ]

    window = sg.Window("Sistema de Control de Gastos", layout, size=(600, 300))


    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "Add Category":
            show_add_category_window(csv_category_file,finance_manager)
        
        elif event == "Add Income":

        #READING FILE AND UPDATING THE TABLE AFTER ADDING INCOME    
            show_add_income_window(csv_mov_file,csv_category_file,finance_manager)
            new_rows=read_source_movements_file(csv_mov_file) 
            window['table'].update(values=new_rows)
    
        elif event == "Add Expense":
            show_add_expense_window(csv_mov_file,csv_category_file,finance_manager)  
            new_rows=read_source_movements_file(csv_mov_file) 
            window['table'].update(values=new_rows)

    window.close()


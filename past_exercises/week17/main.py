from Interface import show_main_window
from Category import Category
from Movement import Movement
from FinanceManager import FinanceManager

if __name__ == "__main__":


    category = Category("")
    movement = Movement("",0,"","")

    finance_manager= FinanceManager(category,movement)

    show_main_window("movements.csv", "categories.csv", finance_manager)
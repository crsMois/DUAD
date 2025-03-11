import csv
import sys

def menu_prompt():

    print("1. Add new game to the list")
    print("2. Exit program")

    try:
        user_option=int(input(f"\n Select one option from the list above:  "))
        execute_user_option(user_option)
    except ValueError as error:
            print(f"\n\n Please insert a number({error})\n\n")
            menu_prompt()


def execute_user_option(user_option):
    

    if (user_option == 1):
        try:
            add_new_game_to_list(get_list())
            menu_prompt()
        except ValueError as error:
            print(f"Please insert a number ({error})")
            menu_prompt()
    elif (user_option == 2):
        try:
            sys.exit()

        except ValueError as error:
            print(f"Please insert a number ({error})")
            menu_prompt()          
    else:
        menu_prompt()


def get_list():
    
    list_games = [
        {
            'name': 'Grand Theft Auto IV',
            'gender': 'Accion',
            'developer' : 'Rockstar Games',
            'clasification': 'M',
        }
    ,
        {
            'name': 'The Elder Scrolls IV: Oblivion',
            'gender': 'RPG',
            'developer' : 'Bethesda',
            'clasification': 'M',
        }
    ,
        {
            'name': 'Tony Hawks Pro Skater 2',
            'gender': 'Deportes',
            'developer' : 'Activision',
            'clasification': 'T',
        }    
    ]

    return list_games


def add_new_game_to_list(list_games): 


    dict_new_game =   {
            'name': '',
            'gender': '',
            'developer' : '',
            'clasification': '',
        }  


    while True:
        try:
            dict_new_game["name"]= input("Enter the game name: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")

    while True:
        try:
            dict_new_game["gender"]= input("Enter the Gender: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")

    while True:
        try:
            dict_new_game["developer"]= input("Enter the developer: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")

    while True:
        try:
            dict_new_game["clasification"]= input("Enter clasification: ")
            break  
        except Exception as error:
            print(f"Please enter an correct value {error}...")   


    list_games.append(dict_new_game)
    create_games_file("Games.csv",list_games)
        

def create_games_file(in_file_to_create, data_list):
    
    with open(in_file_to_create,"w", newline='') as file:
        writer = csv.DictWriter(file, data_list[0].keys(), delimiter=' ')
        writer.writeheader()
        writer.writerows(data_list)
        print("\n\n\n CSV file has been updated with the new game!!!!!! \n\n\n")



def main():
    menu_prompt()


main()
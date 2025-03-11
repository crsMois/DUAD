import json

def ask_user_add_new_pokemon():
    new_pokemon_dict = {
        "name": {"english": ""},
        "type": [""],
        "base": {"HP": 0, 
                "Attack": 0, 
                "Defense": 0, 
                "Sp. Attack": 0, 
                "Sp. Defense": 0, 
                "Speed": 0}
    }


    new_pokemon_dict["name"]["english"] = input("Please enter the new Pokemon name: ")
    new_pokemon_dict["type"][0]= input("What is the Type of this Pokemon: ")
    
    while True:
        try:
            new_pokemon_dict["base"]["HP"]= int(input("Type the HP: "))
            break  
        except ValueError:
            print("Please enter an Integer Value...")


    while True:
        try:
            new_pokemon_dict["base"]["Attack"]= int(input("Type the Attack: "))
            break  
        except ValueError:
            print("Please enter an Integer Value...")


    while True:
        try:
            new_pokemon_dict["base"]["Defense"]= int(input("Type the Defense: "))
            break  
        except ValueError:
            print("Please enter an Integer Value...")

    
    while True:
            try:
                new_pokemon_dict["base"]["Sp. Attack"]= int(input("Type the Sp. Attack: "))
                break  
            except ValueError:
                print("Please enter an Integer Value...")
        
    while True:
            try:
                new_pokemon_dict["base"]["Sp. Defense"]= int(input("Type the Sp. Defense: "))
                break  
            except ValueError:
                print("Please enter an Integer Value...")
            
    while True:
            try:
                new_pokemon_dict["base"]["Speed"]= int(input("Type the Speed: "))
                break  
            except ValueError:
                print("Please enter an Integer Value...")

    return new_pokemon_dict



def open_pokemon_json_file(pokemon_json_file):
    with open(pokemon_json_file,"r") as pokemon_read_file:
        list_pokemons_py=json.load(pokemon_read_file)
        
        return list_pokemons_py


def add_new_pokemon_to_file(list_of_all_pokemon, new_pokemon, pokemon_file):
    list_of_all_pokemon.append(new_pokemon)

    with open(pokemon_file, "w") as pokemon_write_file:
        json.dump(list_of_all_pokemon,pokemon_write_file)



def main():

    pokemon_file="pokemon.json"
    list_pokemon_from_json=open_pokemon_json_file(pokemon_file)
    dict_new_pokemon= ask_user_add_new_pokemon()
    add_new_pokemon_to_file(list_pokemon_from_json,dict_new_pokemon,pokemon_file)




main()

def menu_prompt(currentNumber):

    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Borrar resultado")

    client_option=input (f"\n Select one aritmetic operator from the list above (  {currentNumber}  ):  ")
    
    try:
        select_arithmetic(currentNumber, int(client_option))
    except ValueError as error:
            print(f"Please insert a number({error})")
            menu_prompt(currentNumber)


def select_arithmetic(currentNumber, client_option):
   
    if (client_option == 1):
        try:
            num_sum= input(f"SUMA {currentNumber} + ")
            currentNumber= currentNumber + int(num_sum)
            menu_prompt(currentNumber)
        except ValueError as error:
            print(f"Please insert a number ({error})")
            menu_prompt(currentNumber)

    elif (client_option == 2):
        
        try:
            num_sum= input(f"RESTA {currentNumber} - ")
            currentNumber= currentNumber - int(num_sum)
            menu_prompt(currentNumber)
        except ValueError as error:
            print(f"Please insert a number ({error})")
            menu_prompt(currentNumber)


    elif (client_option == 3):
        
        try:
            num_sum= input(f"MULTIPLICACION {currentNumber} * ")
            currentNumber= currentNumber * int(num_sum)
            menu_prompt(currentNumber)
        except ValueError as error:
            print(f"Please insert a number ({error})")
            menu_prompt(currentNumber)


    elif (client_option == 4):

        try:
            num_sum= input(f"DIVISION {currentNumber} \ ")
            currentNumber= currentNumber / int(num_sum)
            menu_prompt(currentNumber)

        except ValueError as error:
            print(f"Please insert a number ({error})")
            menu_prompt(currentNumber)
        except ZeroDivisionError as error:
            print(f"you can't divide by zero ({error})")
            menu_prompt(currentNumber)

    elif (client_option == 5):

        menu_prompt(0)


def main():
    
        currentNumber=0

        try:
            menu_prompt(0)

        except ValueError as error:
            print(f"Please insert a number ({error})")
            menu_prompt(currentNumber)

main()


class Robot:

    def robotTasks(func):
        def wrapper (self,*args):
            
            paramNumber=1

    #PRINT PARAMS
            for value in args:
                print(f"Param{paramNumber}: {value} ")
                paramNumber += 1
            try:

    #FUNCTION CALL            
                returned_value=func(self,*args)
            except TypeError as error:
                print(f"Print you are missing parameters for the Robot actions please check and add an ingredient if necessary to meet the minimal required")
                returned_value=False

    #PRINT FUNCTION RETURN
            print (f"The returned value of this function is: {returned_value}\n\n")

        return wrapper



    @robotTasks
    def clean(self, ingredient1, ingredient2):
        clean="dirty" 
        if (ingredient1 and ingredient2):
            clean = "Clean"
        return clean
    

    @robotTasks    
    def cook(self, *args):
        food = "Made Meal"
        return food


def main():
    robot1 = Robot()
    robot1.clean("Water","Wax")
    robot1.cook("Rice","Beans","Meat","Salad")


main()
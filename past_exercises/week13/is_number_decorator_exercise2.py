class IsNotNumberException(Exception):
    pass 

class Numbers:


    def test_if_number(func):
        def wrapper(self, *args):
            for value in args:              
            #DETERMINE IF THE VALUE RECEIVED IS A NUMBER
                    if not isinstance(value, (int, float)):
            #THROWING AN ERROR MESSAGE IF IT IS NOT A NUMBER          
                        raise IsNotNumberException("This is not a valid number please check your list and try again")
                        return wrapper
            #RUNNING THE FUNCTION AFTER THE VALIDATION ABOVE IS SUCCESSFUL
            return func(self,*args)

        return wrapper

    @test_if_number
    def sum_numbers(self,*args):
        sum=0
        for number in args:
            sum=sum+number

        return sum


def main():
    sum1 = Numbers()

    try:
        print(sum1.sum_numbers(1,2,4))
    except Exception as e:
        print(f"The required action could not be executed: {e}")

main()
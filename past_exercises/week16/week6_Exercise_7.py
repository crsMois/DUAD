import math

numbers_list = [1, 4, 6, 7, 13, 9, 67]


def validate_if_prime(new_number):
    root = 0
    if ((new_number !=1) and (new_number %2 != 0) and new_number>0):
        root=(math.ceil(math.sqrt(new_number)))
        for index in range(2, root+1):
            if (new_number % index ==0 ):
                return False
    else:
        return False            
    return True


def create_list_prime_numbers(new_list_numbers):
    if not isinstance(new_list_numbers, list) or len(new_list_numbers) < 2:
        raise ValueError("The input must be a list with at least two numbers")
    
    list_primes=[]
    for new_number in new_list_numbers:
        if(validate_if_prime(new_number)):
            list_primes.append(new_number)   
    return list_primes


print(create_list_prime_numbers(numbers_list))
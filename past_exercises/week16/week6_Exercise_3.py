numbers = [4, 6, 2, 29]


def sum_list(numbers_list):
    summation = 0
    for number in numbers_list:
        summation = summation + number

    if numbers_list == [] :
        return numbers_list

    return summation


print(f"the summation of all number in the list above is: {sum_list(numbers)}") 
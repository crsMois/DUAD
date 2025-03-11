my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,11,11,11,11,11,11]
counter = 0

for counter in range(len(my_list)-1,-1,-1):
    if (my_list[counter]%2!=0):
        my_list.pop(counter)


print(my_list)
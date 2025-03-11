my_list = [3, 4, 3, 6, 1, 7, 5, 8]
pivot = my_list[0]
my_list[0]= my_list[len(my_list)-1] 
my_list[len(my_list)-1] = pivot

print ("updated list: ")
print (my_list)    
hight_number = 0
numbers = []


for index in range(0,10):
    user_number=input("please enter number "+ str(index+1) + ": ")
    numbers.append(int(user_number))


for key in range(0,len(numbers)):
    if (numbers[key]> hight_number):
        hight_number= numbers[key]


print (numbers)
print ("The highest number is: " + str(hight_number)  )
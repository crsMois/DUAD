
name= input("Please enter your name: ")
lastname= input("Please enter your lastname: ")
age= int(input("Please enter your su age "))


if (age < 10):
    print ("You are a kid")
elif (age < 15 ):
    print("Your are a preteen")
elif (age < 18 ):
    print("You are teen")
elif (age < 35 ):
    print("You are a Young Adult")
elif (age < 65 ):
    print("You are an Adult")
else:
    print("You are an older Adult")
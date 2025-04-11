from datetime import date

class MinorUserException(Exception):
    pass

class User:

    date_of_birth=date
    marital_status = ""

    def __init__(self, date_of_birth):
        self.date_of_birth= date_of_birth
    

    def validate_if_adult(func):
        def wrapper(user,*args):
            if (user.age<18):
                raise MinorUserException("You are a Minor")
            else:
                print("You are adult, can proceed")
            func(user,*args)
        return wrapper


    @property
    def age(self):
        today = date.today()
        return (today.year - self.date_of_birth.year-((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day)))

    @validate_if_adult
    def set_user_marital_status(self,marital_status):
        self.marital_status=marital_status


def main():
    user1 = User(date(2008, 4, 10))
    print(user1.age)

    try:
        user1.set_user_marital_status("single")
    except MinorUserException as e:
        print(f"The required action could not be executed: {e}")

    print(user1.marital_status)

main()




class Person:

    def __init__(self,name, age):
        self.name=name
        self.age= age


class Bus ():
    
    def __init__(self):
        self.max_passengers=2
        self.list_of_passengers= []
    
    def add_passenger(self,passenger): 
        if (len(self.list_of_passengers) < self.max_passengers):
            self.list_of_passengers.append(passenger)
        else:   
            print("You have reach the max of passengers")

    def get_off_passenger(self, passenger):
        self.list_of_passengers.remove(passenger)
        print(f"\n\nNew list after the passenger {passenger.name} gets off")

    def get_list_passenger(self):
        return self.list_of_passengers

    def print_current_list_of_passengers(self):
            for passenger in self.list_of_passengers:
                print(f"Passenger name: {passenger.name} - age: {passenger.age}")


def main():
    person1= Person("Maria",15)
    person2= Person("Felipe",10)
    person3= Person("Carlo",22)
    
    
    bus1= Bus()
    bus1.add_passenger(person1)
    bus1.add_passenger(person2)
    bus1.add_passenger(person3)
    bus1.print_current_list_of_passengers()
    bus1.add_passenger(person2)

#    bus1.get_off_passenger(person2)
    bus1.print_current_list_of_passengers()


main()


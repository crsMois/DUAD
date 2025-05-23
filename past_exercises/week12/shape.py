from abc import ABC, abstractmethod
import math

class Shape(ABC):

    def __init__(self):
        self.area=0
        self.perimeter=0

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    

    def __init__(self,radius):
        self.radius=radius
        self.circle_pi=math.pi
        
    def calculate_area(self):
        self.area=self.circle_pi*(self.radius**2)
        return self.area

    def calculate_perimeter(self):
        self.perimeter=2*self.circle_pi*self.radius
        return self.perimeter


class Square(Shape):


    def __init__(self,side):
        self.side=side

    def calculate_area(self):
        self.area=self.side**2
        return self.area
    
    def calculate_perimeter(self):
        self.perimeter=4*self.side
        return self.perimeter


class Rectangle(Shape):

    def __init__(self,length, width):
        self.length=length
        self.width=width
    
    def calculate_area(self):
        self.area=self.length*self.width
        return self.area

    def calculate_perimeter(self):
        self.perimeter=2*(self.length+self.width)      
        return self.perimeter
    

def main():

    circle1=Circle(35)
    print(f"The circle area is {circle1.calculate_area()}")
    print(f"The circle perimeter is {circle1.calculate_perimeter()}\n\n")


    square1=Square(25)
    print(f"The Square area is {square1.calculate_area()}")
    print(f"The Square perimeter is {square1.calculate_perimeter()}\n\n")


    rectangle1=Rectangle(10,13)
    print(f"The Rectangle area is {rectangle1.calculate_area()}")
    print(f"The Rectangle perimeter is {rectangle1.calculate_perimeter()}")


main()
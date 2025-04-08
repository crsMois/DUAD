import math

class circle:
    radius=0
    pi=math.pi
    
    
    def __init__(self, radius):
        self.radius=radius

    def get_area(self):
        area=self.pi * (self.radius **2)
        
        return area

def main():         
    circle1 = circle(25)
    circle1_area=circle1.get_area()
    print(circle1_area)


main ()
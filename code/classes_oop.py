#Classes Challenge
import math
class Rectangle:
    def __init__(self, height = 0, width = 0):
        self._height = height
        self._width = width
    
    @property
    def height(self):
        print("getter method is called")
        return self._height
    
    @property
    def width(self):
        print("getter method is called")
        return self._width
    
    @height.setter
    def height(self, value):
        if value.isdigit():
            print("Height was set with the setter")
            self._height = value
        else:
            print("height must be an integer")
    
    @width.setter
    def width(self, value):
        if value.isdigit():
            print("width was set with the setter")
            self._width = value
        else:
            print("width must be an integer")

    def get_area(self):
        return int(self._height) * int(self._width)

new_rectangle = Rectangle(5, 4)
user_w=input("Please Enter Width: ")
user_h=input("Please Enter Height: ")
new_rectangle.height = user_h
new_rectangle.width = user_w



#OOP Challenge
class Vehicle:
    def __init__(self, vehicle_type = ""):
        self.vehicle_type = vehicle_type
    
    def drive(self):
        print("There are many kinds of vehicles. Vehicles are mobiles that can drive.")

class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)
        self.name = name
    
    def getInfo(self):
        print(f"This vehicle is a {self.name}")


def main():
    print(new_rectangle.width)
    print(new_rectangle.height)
    print("area = ", new_rectangle.get_area())
    my_vehicle = Vehicle()
    my_car = Car("Civic")
    my_car.getInfo()

if __name__ == "__main__":
    main()





# class Person:
#     name = "Ben"
#     age = 37
#     def intro(self):
#         print(f"My name is {self.name} and I am {self.age} years old")

# person = Person()
# print(person.name)
# print(person.age)
# person.name = "Tom"
# print(person.name)

# person.intro()

# class Cat:
#     def __init__(self, name = "Boots", breed = "Alley cat", age = 7):
#         self.name = name
#         self.breed = breed
#         self.age = age
#     def meow(self):
#         return "{} goes 'MEEEOOOOWWWW'".format(self.name)

# zeal = Cat("Zeal", "Street Cat", 2)
# ardor = Cat("Ardor", "Street Cat", 2)
# indy = Cat("Indy", "Alley Cat", 7)
# boots = Cat()

# def main():
#     print(zeal.name)
#     print(ardor.name)
#     print(boots.name)
#     print(indy.name)
#     print(zeal.meow())

# if __name__ == "__main__":
#     main()

# from datetime import date

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def fromBirthYear(cls, name, year):
#         return cls(name, date.today().year, year)

#     @staticmethod
#     def isAdult(age):
#         return age > 18

# person1 = Person("Ben", 37)
# person2 = Person.fromBirthYear("Allen", 1982)

# def main():
#     print(person1.name)
#     print(person2.name)
#     print(person1.isAdult(person1.age))

# if __name__ == "__main__":
#     main()

# import math

# class Circle:
#     def __init__(self, radius = 0):
#         self._radius = radius

#     @property
#     def radius(self):
#         print("getter method is called")
#         return self._radius
        
#     @radius.setter
#     def radius(self, value):
#         if value.isdigit():
#             print("radius was set with the setter")
#             self._radius = value
#         else:
#             print("radius must be an integer")

#     def get_area(self):
#         return pow(int(self._radius), 2) * math.pi

# new_circle = Circle(10)
# user_r = input("Please enter radius: ")
# new_circle.radius = user_r

# def main():
#     print("radius = ", new_circle.radius)
#     print("The area of the circle is:", new_circle.get_area())


# if __name__ == "__main__":
#     main()

# class Person:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
    
#     def print_name(self):
#         print(f"My name is {self.first_name} {self.last_name}")

# class Coach(Person):
#     def __init__(self, first_name, last_name, cohort):

#         super().__init__(first_name, last_name)
#         self.cohort = cohort
#     def welcome(self):
#         print(f"Welcome to the {self.cohort}. I am your coach {self.first_name} {self.last_name}")
    
# ben_person = Person("Ben", "Bruton")
# ben_coach = Coach("Benjamin", "Bruton", "ASML")
# def main():
#     print(ben_person.first_name)
#     ben_person.print_name()
#     print(ben_coach.first_name)
#     ben_coach.welcome()


# if __name__ == "__main__":
#     main()

# class Bird:
#     def __init__(self, name = ""):
#         self.name = name
    
#     def flight(self):
#         print("There are many kinds of birds. Some birds fly. Some cannot.")
    
# class Sparrow(Bird):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def flight(self):
#         print(f"A {self.name} can fly.")
# class Ostrich(Bird):
#     def __init__(self, name):
#         super().__init__(name)
    
#     def flight(self):
#         print(f"An {self.name} cannot fly.")

# bird = Bird()
# sparrow = Sparrow("sparrow")
# ostrich = Ostrich("ostrich")

# def main():
#     bird.flight()
#     sparrow.flight()
#     ostrich.flight()

# if __name__ == "__main__":
#     main()

# class Wallet:
#     def __init__(self, value, unit="USD"):
#         self.value = value
#         self.unit = unit

#     def __str__(self):
#         return f"{self.value} {self.unit}"

#     def __add__(self, value2):
#         return Wallet(self.value + value2.value)

# my_wallet = Wallet(5000)

# another_wallet = Wallet(100)
# third_wallet = my_wallet + another_wallet

# print(another_wallet)

# print(my_wallet.value)
# print(third_wallet)
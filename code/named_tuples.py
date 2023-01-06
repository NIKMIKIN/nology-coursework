#Stationary Store Challenge
from collections import namedtuple

Pens = namedtuple("Pens", "size inkcolor beveled")
standard_Pen = Pens(2, "Black", True)
red_Pen = Pens(2, "Red", True)
whiteboard_Pen = Pens(4, "Black", False)
print(f"Standard Pen: size = {standard_Pen.size}, ink = {standard_Pen.inkcolor}, is beveled = {standard_Pen.beveled}")
print(f"Red Pen: size = {red_Pen.size}, ink = {red_Pen.inkcolor}, is beveled = {red_Pen.beveled}")
print(f"WhiteBoard Pen: size = {whiteboard_Pen.size}, ink = {whiteboard_Pen.inkcolor}, is beveled = {whiteboard_Pen.beveled}")

#Slope of a Line Challenge
Point = namedtuple('Point', ['x','y'])
p1 = Point(x=2 , y=1)
p2 = Point(x=4, y=7)
def slope(p1, p2):
    result = (p2.y-p1.y)/(p2.x-p1.x)
    return result

print(f"({p2.y} - {p1.y}) / ({p2.x} - {p1.x}) = {slope(p1, p2)}")

# from collections import namedtuple


# Point = namedtuple('Point', ['x', 'y'])
# p = Point(x=11, y=22)

# print(type(Point))

# print(p[0])
# print(p[1])

# x, y = p
# print(x,y)

# print(p.x, p.y)

# from collections import namedtuple

# EmployeeRecord = namedtuple("EmployeeRecord", "name age title")
# emp_rec = EmployeeRecord("Michael Corleone", 45, "The Godfather")

# print(f"{emp_rec.name} is the new {emp_rec.title}")

# Parent = namedtuple("Parent", "name children")

# vito = Parent("Vito Corleone", ["Sonny", "Michael"])

# Developer = namedtuple("Developer", "name level language", defaults= ["Junior", "Python"])

# dev = Developer("Steve")

# print(f"{dev.name} is a {dev.level} developer in {dev.language}")

# from collections import namedtuple

# Person = namedtuple("Person", "name age height")
# john = Person._make(["John", 25, 1.75])

# joe_bob = Person("Joe Bob", 30, 72)

# print(john)
# print(joe_bob._asdict())

# jane = joe_bob._replace(name="Jane")

# print(jane)

# ExtendedPerson = namedtuple("ExtendedPerson", [*Person._fields, "weight"])

# halfThor = ExtendedPerson("halfThor", 28, 82, 325)

# print(halfThor.weight)

# for field, value in zip(halfThor._fields, halfThor):
#     print(field, "=", value)



# car = (4, "Gray", True)

# if car[0] == 4 and car[1] == "Gray" and car[2]:
#     print("Gray sedan selected")

# from collections import namedtuple

# Car = namedtuple("Car", "doors color isAvailable")
# car = Car(4, "Gray", True)

# if car.doors == 4 and car.color == "Gray" and car.isAvailable:
#     print("Gray Sedan selected")

# print(divmod(9,4))

# def custom_divmod(a, b):
#     Divmod = namedtuple("DivMod", "quotient remainder")
#     return DivMod(*divmod(a,b))

#print(custom_divmod(8, 4))
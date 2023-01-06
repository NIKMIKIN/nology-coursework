#Functions Challenge
def my_first_function(args):
    print(f"I love {args}")
my_first_function("Nik")

#Lambdas Challenge
given_list = [2, 5, 7, 32, 100, 9, 56, 74, 97, 22, 13, 80]

even_values = list(filter(lambda x: x % 2 == 0, given_list))
print(even_values)


trippled_list = list(map(lambda x: x * 3, given_list))
print(trippled_list)

from functools import reduce
sum_of_list = reduce(lambda a, b: a + b, given_list)
print(sum_of_list)

#Advanced Functions
def is_palindrome(palindrome):
    palindrome = palindrome.lower().replace(' ', '')
    return palindrome == palindrome[::-1]

answers = []

def list_of_strings(*args):
    for arg in args:
        answers.append(is_palindrome(arg))

list_of_strings("racecar", "max", "kayak", "sword", "radar")
print(answers)















# def set_name():
#     name = "Ben"
#     print(name)

# set_name()

# def change_name():
#     global global_name
#     global_name = "Ollie"

# global_name = "Rich"
# change_name()
# print(global_name)

# x = lambda a, b, c: a + b - c
# print(x(2,2,5))

# def func(n):
#     return lambda x: x * n

# doubler = func(2)
# print(doubler(10))

# trippler = func(3)
# print(trippler(10))

# from math import pi as pie

# def circle_perimeter(radius):
#     return 2 * pie * radius
# print(circle_perimeter(10))

# my_list = [2.99,3.50,4.95,5.25,6.99,7.95,8.50,9.01,10.01]

# modified_list = list(map(lambda x: round(x * 1.0825, 2), my_list))

# print(my_list)
# print(modified_list)

# new_list = range(1, 21)
# evens = list(filter(lambda x: x % 2 == 0, new_list))
# odds = list(filter(lambda x: x % 2 != 0, new_list))

# print(list(new_list))
# print(evens)
# print(odds)

# from functools import reduce

# new_list = [1,2,3,4,5,6,7,8,9]

# product_list = list(range(1,10))

# sum1 = reduce(lambda a, b: a + b, new_list)
# product = reduce(lambda a, b: a * b, product_list)

# print(sum1)
# print(product)

# favorites = []
# def my_args(arg1, arg2, arg3, arg4, *args):
#     print("F Name ", arg1)
#     print("L Name ", arg2)
#     print("Email ", arg3)
#     print("Phone ", arg4)
    
#     for arg in args:
#         favorites.append(arg)
        
# first_name = "Ben"
# last_name = "Brutal"
# email = "ben.burton@nology.io"
# phone = "555-555-5555"
# favorite_key = "house"
# favorite_computer = "mine"
# favorite_sport = "water polo"
# favorite_kidney = "right"


# my_args(first_name, last_name, email, phone, favorite_key, favorite_computer, favorite_sport, favorite_kidney)
# print(favorites)

# def my_function(**friend):
#     print("My best friends name is {}. He lives at {}".format(friend["name"], friend["address"]))
#     print(f"My best friends name is {friend['name']}. He lives at {friend['address']}")

# my_function(name="Joe", address="123 Main St.")

# def keyword_function(**kwargs):
#     for k, v in kwargs.items():
#         print(f"{k} : {v}")

# keyword_function(firstname = "Herbie", lastname = "Hoover", age = 45, email = "herb.hooves@gmail.com")

# def intro(**kwargs):
#     for key, value in kwargs.items():
#         print(f"My {key} is {value}")

# intro(firstName = "Slim", lastName = "Shady", age = 21, number = 1234567890)
# intro(firstName = "James", lastName = "Bond", age = 40, email = "James.jamesbond@sas.uk", country = "England")


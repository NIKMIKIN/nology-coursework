#lists challenge
import array as arr
my_array = [[0] * 10 for i in range(10)]
print(my_array)
for i in range(0,10):
    for j in range(0,10):
        my_array[i][j] = (i+1)*(j+1)
for i in my_array:
    print(i)  

#tuples challenge
historical_figures = 'Vladimir Lenin', 'Thomas Jefferson', 'Barack Obama', 'Tsar Nicolas III', 'John Curtin'
a, b, c, d, e = historical_figures
my_dictionary = {
    "Russia" : [a, d],
    "US" : [b, c,], 
    "Australia" : [e],

}
for k, v in my_dictionary.items():
    print(f"(Country) {k} : {v}")

#Dictionaries Challenge
customers_array = []
while True:
    user_input = input("Enter another name?: (Yes/No) ")
    user_input = user_input[0].lower()
    if user_input == 'n':
        break
    else:
        first_name, last_name = input("Enter your name (first/last): ").split()
        customers_array.append({"first name": first_name, "last name": last_name})
for i in customers_array:
    print(i["first name"], i["last name"])

#Loops Challenge
for i in range(1, 16):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

# my_nums = [4, 2, 3, 1, 5]

# print(type(my_nums))

# print(my_nums[-1])
# print(my_nums[1])

# my_nums.pop(2)
# my_nums.insert(1, 7)
# my_nums.sort
# print(my_nums[-3::])
# my_word = "example string"
# print(my_word[-3::])

# import array as arr
# fruits = iter(["apple", "banana", "peach", "cherry"])

# print(next(fruits))
# print(next(fruits))
# print(next(fruits))
# print(next(fruits))

# my_tuple = (1, 2, 3, 4, 5)
# my_list = [1, 2, 3, 4, 5]
# my_tuple = tuple(my_list)
# changing_tuple = ([1,2,3], [4,5,6])
# print(changing_tuple[0].append(4))

# print(changing_tuple)

# my_other_tuple = 1, 2, 3, 4, 5

# print(type(my_other_tuple))

# my_tuple = 123, 321, "hello!"

# x, y, z = my_tuple

# print(x)
# print(z)
# print(y)

# my_dictionary = {
#     "first_name": "Barack",
#     "last_name": "Obama",
#     "address": "17 Pennsylvania Ave.",
# }

# fruits = ["apple", "banana", "cherry", "orange", "peach"]

# for fruit in fruits:
#     if fruit == "cherry":
#         continue
#     print(fruit)
    

# words = "this is a string"

# for letter in words:
#     print(letter)

# for n in range(1, 10):
#     if n % 2 == 0:
#         print(n)

# x = 0

# while x < 10:
#     x += 1
#     if x == 6:
#         continue
#     print(x)

# print(my_nums)
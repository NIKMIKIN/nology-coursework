# import entry_points

# print(entry_points.is_palindrome("racecar"))
# print(entry_points.is_palindrome("sword"))
# print(entry_points.is_palindrome("civic"))

# Write a function in Python that accepts a list of any length that 
# contains a mix of non-negative integers and strings. The function should return a list with 
# only the integers in the original list in the same order.
def return_integers(mixed_list):
    
    for i in mixed_list:
        if type(i) != int:
            mixed_list.remove(i)
        
    return mixed_list

random_list = [5, 4, 10, "oaisd", 83, "bob"]
print(return_integers(random_list))

# Write a function in Python that accepts a credit card number.
# It should return a string where all the characters are hidden with an asterisk except the last four.
# For example, if the function gets sent "4444444444444444", then it should return "***********4444"

# def transform_card(number):
#     new_card = ""
    
#     for i in range(0,len(number)):
#         if i < len(number)-3:
#             new_card+="*"
#         else:
#             new_card+=number[i]
#         return new_card


# card = 4444444444444444
# print(transform_card(card))

# print("in entry points2")
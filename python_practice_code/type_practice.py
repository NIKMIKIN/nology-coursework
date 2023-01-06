#Types
my_num = float(input("Enter a number: "))
print(my_num)

result = int(my_num/int(input("Enter a number to divide our previous number: ")))
print(result)

name = input("Enter a name: ")
print(f"Hello {name}!")

#Strings
f_name = input("Enter the first name of your coach: ")
l_name = input("Enter the last name of your coach: ")

f_initial = f_name[0].upper()
l_initial = l_name[0].upper()

initials = f_initial + "." + l_initial
print(initials)

#Control FLow
age = 0

for i in range(0, 3):
    age = int(input("Enter age of student: "))
    if age < 5:
        print("no school")
    elif age > 5 and age <=18:
        grade = age-5
        print(f"grade: {grade}")
    elif age > 18:
        print("go to university")
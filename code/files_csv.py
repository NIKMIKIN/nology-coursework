import os
import csv
import pandas as pd


#Files Challenge
with open("newfile.txt", encoding="utf-8") as my_file:
    line_num = 1
    while True:
        line = my_file.readline()
        if not line:
            break
        words = len(line.split())
        print("Line # : ", line_num, " | ", line, " # of Words: ", words, end="\n")


# California,9600500   
# Texas,29700300   
# Florida,21900500   
# New York,19900500   
# Pennsylvania,12800100   
# Illinois,12500300   
# Ohio,11700600   
# Georgia,10800000   
# North Carolina,10700000   
# Michigan,9900400  


#CSV Challenge
header = ['Capital', 'State', 'Population']
data = [['Sacramento','California',9600500], ['Austin','Texas',29700300  ], ['Tallahasse','Florida',21900500   ], ['Albany','New York',19900500],
 ['Harrisburg', 'Pennsylvania',12800100], ['Springfield', 'Illinois',12500300 ], ['Colombus', 'Ohio',11700600], ['Atlanta','Georgia',10800000], 
 ['Raleigh', 'North Carolina',10700000], ['Lansing', 'Michigan',9900400]]

rows = []
with open('unitedStates.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)
with open('unitedStates.csv', mode="w", newline = '') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(data)

print(f"The headers are: {header}")
print(rows)


# example_dictionary = {'name': ["Rich", "Ash", "Ben", "Steph"], 'age':[35, 26, 37, 26],
# 'designation': ["Head of US", "Lead Coach", "Instructor", "A.Instructor"]}

# df = pd.DataFrame(example_dictionary)
# print(df)

# df.to_csv("csv_example", index = False)

# new_df = pd.read_csv("csv_example")

# print(new_df)

# data = {
#     'col1': [10, 20, 30],
#     'col2': ['A', 'B', 'C']
# }

# print(data)

# df = pd.DataFrame(data)

# print(df.to_json())
# df.to_json("example_json")

# header = ['Name', 'age']
# data = [['Alex', 25], ['Brad', 30], ['Joey', 18]]
# with open('student_info.csv', mode= 'w', newline='') as csvfile:
#     csvwriter: 

# rows = []
# with open('employers.csv', newline='') as csvfile:
#     csvreader = csv.reader(csvfile)
#     header = next(csvreader)
#     for row in csvreader:
#         rows.append(row)
    
# print(f"The headerse are: {header}")
# print(rows)


# with open("newfile.txt", encoding="utf-8") as my_file:
#     line_num = 1
#     while True: # readline() will read one line at a time
#         line = my_file.readline()
#         if not line:
#             break
#         print("Line # : ", line_num, " | ", line, end="")
#         line_num+=1

#os.mkdir("myDirectory")

# os.chdir("myDirectory")

# print("current working directory:", os.getcwd())

# with open("myfile.txt", mode = "w", encoding="utf-8") as my_file:
#     my_file.write("Some text\nMore text\neven more")
# with open("myfile.txt", encoding="utf-8") as my_file:
#     print(my_file.read())

# print(my_file.name)
# print(my_file.mode)

# my_file.close()

# os.rename("myfile.txt", "newfile.txt")
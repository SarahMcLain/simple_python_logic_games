# name = input("what's your name?")

# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# with open("names.txt", "r") as file:
#     lines = file.readlines()

# for line in lines:
#     print("hello,", line.rstrip())

# with open("names.txt", "r") as file:
#     for line in file:
#         print("Hello,", line.rstrip())

# names = [] 

# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())

# for name in sorted(names):
#     print(f"hello, {name}")

# with open("names.csv") as file:
#     for line in sorted(file, reverse=True):
#         print("hello,", line.rstrip())

# with open("names.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# with open("names.csv") as file:
#     for line in sorted(file):
#         name, house = line.rstrip().split(",")
#         print(f"Hello, {name}, you will be in {house}")

students = []

# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)
# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# students = []
# with open("names.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name,
#                    "house": house}
#         students.append(student)


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")


import csv

# students = []

# with open("names.csv") as file:
#     reader = csv.reader(file)
#     for name, house, home in reader:
#         students.append({"name": name, "house": house, "home": home})
    
# for student in sorted(students, key=lambda student: student["name"]):
#      print(f"{student['name']} is in {student['house']} and grew up in {student['home']}")

students= []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
      print(f"{student['name']} is in {student['house']} and grew up in {student['home']}")

students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "jack russel terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None}

]

for student in students:
    print(student["name"], student["house"], student['patronus'], sep=", ")

#case and match example
# name = input('What is your name?')

# match name:
#     case 'Harry' | "Hermione":
#         print("gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")


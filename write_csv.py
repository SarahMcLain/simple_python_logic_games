import csv

name = input("What's your name?")
house = input("What's your house?")
home = input("Where did you grow up?")

with open("names.csv", "a") as file:
    # writer = csv.writer(file)
    # writer.writerow([name, house, home])
    writer = csv.DictWriter(file, fieldnames=["name", "house", "home"])
    writer.writerow({"name": name, "house": house, "home": home})

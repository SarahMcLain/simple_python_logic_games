# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
            return x
        except ValueError:
            pass
            #print("x needs to be integer")
main()
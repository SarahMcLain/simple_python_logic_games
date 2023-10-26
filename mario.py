# def main(n):
#     print_column(n)


# def print_column(height):
#     for _ in range(height):
#         print('#')

# def main():
#     print_row(4)

# def print_row(width):
#     print("?" * width)

# main()

# def main(n):
#     print_square(n)

# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print('#', end="")
#         print()
# main(6)
        
def main(n):
    print_square(n)
def print_square(size):
    for _ in range(size):
        print('#' * size)
main(3)
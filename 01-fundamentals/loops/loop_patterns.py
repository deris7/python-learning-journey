#prints column of bricks using a loop
for _ in range(3):
    print("#")

# Prints column of bricks using a function with a loop
print("---------------------------")
def main():
    print_column(3)

def print_column(height):
    for _ in range (height):
        print("#")

main()

#Prints column of bricks using a function with str multiplication
print("---------------------------")
def main():
    print_column(3)

def print_column(height):
    print("#\n" * height, end="")

main()

# Prints row of coins using a function with str multiplication
print("---------------------------")
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()

#Prints square of bricks using a function with nested loops
print("---------------------------")
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

main()  


# Prints square of bricks using a function wih a loop and str multiplication
print("---------------------------")

def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print("#" * size)
main()

# Prints square of bricks using a function with a loop and str multiplication
print("---------------------------")

def main():
    print_square(3)

def print_square(size):
    for _ in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()
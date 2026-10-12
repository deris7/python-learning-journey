#demonstrate function without parameter
# def hello():
#     print("Hello!, ")
# name = input("what's your name? ").title()
# hello()
# print(name)

#defining a function with a paramter
# def hello(to):
#     print("Hello!,", to)

# name = input("what's your name? ").strip().title()
# hello(name)

#defining a function with a parameter with a default value
# def hello(to="world"):
#     print("hello,", to)

# hello()
# name = input("what's your name? ")
# hello(name)

#demonstrate defining a main function

def main():
    name = input("What's yor name? ").strip().title()
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()
#Functions uses break and returns
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x

main()

#removes break
print("================Without break================")
def main2():
    x = get_int2()
    print(f"x is {x}")
def get_int2():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main2()
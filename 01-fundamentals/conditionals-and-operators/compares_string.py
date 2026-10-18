# Compares strings
answer = input("Do you agree? ")
if answer == "yes":
    print("Agreed")
else:
    print("Not agreed")

# Compares multiple strings
answer = input("Do you agree? ").strip().lower()
if answer == "yes" or answer == "y":
    print("Agreed")
else:
    print("Not agreed")

# Compares multiple strings
answer = input("Do you agree? ").strip().lower()
if answer.startswith("y"):
    print("Agreed")
else:
    print("Not agreed")
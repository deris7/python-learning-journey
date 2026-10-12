#Ask user for their name 
name = input("What's your name? ")

#Remove whitespace from str
name = name.strip()

#Capitalize user's name
name = name.title()

#say hello to user
print(f"hello, {name}")

#we can combine it in a single line
name2 = input("What's your name? ").strip().title()
print(f"hello, {name2}")

#split user's name into firs and last name
first, last = name2.split()
print(f"{first} is your first name")
print(f"{last} is your last name")
#Demonstrate nesting of funcion calls
# x = int(input("what's x? "))
# y = int(input("what's y? "))

# z = x + y

# print(f"{x} + {y} is {z}")

# #combine in one line 
# print(int(input("what's x? ")) + int(input("what's y? "))) #not recomended, espcially in complex program

#Demonstrate conversion of str to float
x = float(input("what's x? "))
y = float(input("what's y? "))

z = x + y

print(z)

#Demonstrate rouning to nearest int
print("Rounded number")
z = round(x+y)
print(z)

#formatting with commas (for up thousand ex. 1,000)
print("formatting with commas")
print(f"{z:,}")
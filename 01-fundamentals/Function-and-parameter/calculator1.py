#demonstrate division
x = float(input("what's x? "))
y = float(input("what's y? "))

z = x/y
print(z)

#rounding after the decimal point
z = round(x/y,2)
print(z)

#formatting after the decimal  place
z = x/y
print(f"{z:.2f}")
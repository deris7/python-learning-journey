x = int(input("what's x? "))
y = int(input("what's y? "))

if x < y :
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

#inequalities and logical operatpr

if x < y or x > y:
    print("x is not equal to y")
else: 
    print("x is equal to y")

#demonstrates equality
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")

#demonstrate inequality
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Demonstrates inequalities and logical operators
score = int(input("Score: "))
if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
        print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")

# Demonstrates modulo operator
x = int(input("What's x? "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")
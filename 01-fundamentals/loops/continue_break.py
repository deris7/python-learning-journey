#introduces continue, break
while True:
    n = int(input("what's n? "))
    if n <=0:
        continue
    else:
        break


for _ in range(n):
    print("meow")

#Removes continue 
while True:
    n = int(input("what's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

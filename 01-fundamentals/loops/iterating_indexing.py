# Demonstrate indexing into a list
students = ['Hermione','Harry', 'Ron']

print(students[0])
print(students[1])
print(students[2])

#demonstrates iterating over a list
print('------------------------------')
for student in students:
    print(student)

# demonstrate iterating over and indexing into a list
print('------------------------------')
for i in range(len(students)):
    print(i + 1, students[i])

# Demonstarte indexing into a dict
print('------------------------------')
students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])


# Demonstrates iteratig and indexing into a dict
print('------------------------------')
for student in students:
    print(student, students[student], sep=", ")

#Demonstrate iterating over a list of dict objects
print('------------------------------')
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell terrier"},
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
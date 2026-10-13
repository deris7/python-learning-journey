#concatenating strings
#demonstrate how combined two strings with plus operator
my_str_1 = 'Hello'
my_str_2 = "World"

str_plus_str = my_str_1 + ' ' + my_str_2
print(str_plus_str) 

#Repeating strings
sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) 

#concatinating strings with numbers
name = 'Deris P'
age = 24

name_and_age = name + str(age)
print(name_and_age)

#String interpolation
print(f'my name is {name}, and my age is {age}')
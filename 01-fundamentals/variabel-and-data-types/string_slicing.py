#slicing string[start:stop]
my_str = 'Hello world'
print(my_str[1:4])
print(my_str[:7]) #Hello w
print(my_str[8:]) #rld

# step parameter, which is used to specify the increment between each index in the slice.
#string[start:stop:step]
my_str = 'Hello world'
print(my_str[0:11:2]) #Hlowrd
#to reverse a string by setting step to -1, and leaving start and stop blank
my_str = 'Hello world'
print(my_str[::-1])
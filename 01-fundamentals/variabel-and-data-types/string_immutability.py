#how to write multi line string
my_str = """This is multi
line string"""
print(my_str)

#use the opposite kind of quotes
msg = "It's a sunny day"
quote = 'she said, "Hello world!"'
#with a backslash (\)
msg = 'It\'s a sunny day'
quote = "she said, \"Hello world!\""

#Python provides the in operator, which returns a boolean that specifies whether the character or characters exist in the string or not.
my_str = 'Hello world'
print('Hello' in my_str)  # True
print('hey' in my_str)    # False

#use built-in len() to get the length of a string
my_str = 'Hello world'
print(len(my_str)) 

#access character by its index
my_str = "Hello world"
print(my_str[0]) 
print(my_str[6]) 

#immutable string in python
greeting = 'hi'
greeting = 'hello'
print(greeting)
greeting = "Y" + greeting[1:]
print(greeting)
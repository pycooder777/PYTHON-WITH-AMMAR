x = 10          # integer 
y = 10.2        # float
z = "Hello"     # strings

print(type(x))
print(type(y))
print(type(z))

# implicit type conversion
x = x+y
print(x , "the type of x is ",type(x))

# explicit type conversion
age = int(input("what is your age ? "))
print(age , "the type of age is ",type(age))

# Name
name = input("what is yur name ? ")
print(name , "the type of name is ",type(name))
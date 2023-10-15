# Functions 

# Setp 1
def print_codanics():
    print("we are learning with Ammar")
    print("we are learning with Ammar")
    print("we are learning with Ammar")

print_codanics()

# Setp 2
def print_codanics():
     text = "we are learning with Ammar"
     print(text)
     print(text)
     print(text)

print_codanics()

# Setp 3
def print_codanics(text):
     print(text)

print_codanics("We are learning with Ammar from youtube channel")

# defining a function with if , elif and else statement

def school_calculator(age):
    if age == 5:
        print("you can join the school")
    elif age > 5:
        print("you can join the higher school")
    else:
        print("you cannot join the school")

school_calculator(10)

# defining a function of future
def future_age(age):
    new_age = age + 20
    return new_age
future_predicated_age = future_age(18)
print(future_predicated_age)
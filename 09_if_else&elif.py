required_age_school = 6
user_age = int(input("pz Enter a age : "))

# Question can user joined school 

if user_age == required_age_school:
    print("you can joined this school.")
elif user_age > required_age_school:
    print("you can joined higher class. ")
else :
    print("you cannot joined this school because your age is not applicable.")
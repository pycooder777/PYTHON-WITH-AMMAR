# While and For loops

# while loop
x = 0
while (x<=5):
    print(x)
    x += 1

# for loop
for x in range(5,10):
    print(x)

# Array
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
for day in days:
    if (day == "friday"):
        break  # break the loop
    if (day == "friday"): continue   # skip the loop 
    print(day)


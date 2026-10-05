age = int(input("Enter your age: "))
if age < 0:
    print("Invalid Age")
elif age >= 18:
    print("Age is valid")
    print("You are eligible for voting")
else:
    print("Age is valid")
    print("You are not eligible for voting")
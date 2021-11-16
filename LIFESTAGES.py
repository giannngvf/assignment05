print("This program will tell you what stage of life you are in based on your age.")
age = int(input("Enter your age: "))

if  0 <= age <= 12:
    print("You are a kid.")
elif 13 <= age <= 17:
    print("You are a teen.")
elif age == 18:
    print("You are in debut stage.")
else:
    print("You are already an adult.")

print("Now that you know what stage of life you are in, always remember to live your life to the fullest.")
    
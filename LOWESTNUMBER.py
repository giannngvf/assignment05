print("This program will find out the lowest number on the 3 numbers you input.")
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

if second_number > first_number < third_number:
    print(f"The lowest number is {first_number}.")
elif first_number > second_number < third_number:
    print(f"The lowest number is {second_number}.")
elif first_number > third_number < second_number:
    print(f"The lowest number is {third_number}.")
else:
    print("Sorry, we can't identify what's the lowest number if all the numbers you input are the same.")

print("Done. Thank you!")

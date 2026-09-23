# Practice Question 8 - Simple Eligibility Checker
# Check eligibility based on age and citizenship.

age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ")

if age >= 18 and citizenship == "Indian":
    print("You are eligible.")
else:
    print("You are not eligible.")
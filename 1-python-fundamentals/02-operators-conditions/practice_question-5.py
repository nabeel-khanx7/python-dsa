# Practice Question 5 - Grade Calculator
# Calculate grade based on marks from 0 to 100.

marks = float(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print("Invalid marks.")

elif marks >= 90:
    print("Grade: A")

elif marks >= 75:
    print("Grade: B")

elif marks >= 60:
    print("Grade: C")

elif marks >= 40:
    print("Grade: D")

else:
    print("Grade: F")
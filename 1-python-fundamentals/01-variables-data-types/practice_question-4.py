#Q4. Marks Calculator
#Write a Python program that takes the marks of five subjects as input and calculates:
#Total marks
#Average marks
#Percentage
#Assume each subject is out of 100. 

mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))
mark4 = float(input("Enter marks for Subject 4: "))
mark5 = float(input("Enter marks for Subject 5: "))

total = mark1 + mark2 + mark3 + mark4 + mark5
average = total / 5
percentage = (total / 500) * 100

print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
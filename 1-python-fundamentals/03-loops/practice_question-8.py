# Practice Question 8 - Search an Element

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter the number to search: "))

found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Element found.")
else:
    print("Element not found.")
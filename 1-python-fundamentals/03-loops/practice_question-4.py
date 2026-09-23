# Practice Question 4 - Count Even Numbers

count = 0

for number in range(1, 51):
    if number % 2 == 0:
        print(number)
        count += 1

print("Total even numbers:", count)
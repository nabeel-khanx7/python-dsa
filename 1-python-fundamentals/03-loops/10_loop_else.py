# Else with For Loop

for number in range(1, 6):
    print(number)
else:
    print("Loop completed successfully.")


# Else with Break

for number in range(1, 6):
    if number == 3:
        break

    print(number)
else:
    print("Loop completed successfully.")
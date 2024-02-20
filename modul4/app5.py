number_of_participants = int(input("Type the number of the participants: "))
ages = []
i = 1
while i <= number_of_participants:
    try:
        age = int(input(f"Type the age of the participant {i}: "))
    except ValueError:
        print(f"Invalid format of the participant {i}. Type again.")
        continue
    i += 1
    ages.append(age)


def avg(list_of_numbers):
    total = sum(list_of_numbers)
    average_age = total / len(list_of_numbers)
    return average_age


print(avg(ages))


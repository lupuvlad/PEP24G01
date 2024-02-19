def medie(numbers_list):
    return sum(numbers_list) / len(numbers_list)


def suma(numbers_list):
    return sum(numbers_list)


def putere(numbers_list):
    power_list = []
    for num in numbers_list:
        power_list.append(num ** 2)
    return power_list


meniu = {
    "1": medie,
    "2": suma,
    "3": putere
}

num_list = []
while True:
    number = input("Type a number: ")
    if number.lower() == "x":
        break
    try:
        number = float(number)
    except Exception:
        print("Invalid number. Type again")
        continue
    num_list.append(number)

options = {1: "Average", 2: "Sum", 3: "Power", 4: "Exit"}

for option_number, option_name in options.items():
    print(f"{option_number}. {option_name}")

choice = input("Type an option: ")
result = meniu.get(choice)(num_list)
print(f"Result = {result}")


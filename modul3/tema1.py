import time

options = [["1", "cappuccino", 4], ["2", "espresso", 3.5]]

for i, product in enumerate(options):
    print(f"{product[0]}. {product[1].capitalize()}... {product[2]} lei")

user_option = input(f"Choose an option ({'/'.join([value[0] for value in options])}): ")

for option in options:
    idx = option[0]
    coffee = option[1]
    price = option[2]
    if user_option == idx:
        pay = int(input("Insert only 5 or 10 lei: "))
        if pay in [5, 10]:
            change = pay - price
            print(f"You will receive {change} lei change.")
            print(f"Preparing your {coffee}...")
            time.sleep(3)
            print(f"Enjoy your {coffee}!")
            break
        else:
            print("The coffee machine accepts only bank-notes of 5 or 10 lei.")
            break
else:
    print("This option doesn't exist")

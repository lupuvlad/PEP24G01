import time

options = [["1", 4], ["2", 3.5]]

print(f"""1. Cappuccino ... 4 lei
2. Espresso ... 3.5 lei""")
user_option = input("Choose an option (1 or 2): ")

for option in options:
    if user_option == option[0]:
        total = int(input("Insert only 5 or 10 lei: "))
        if total == 5 or total == 10:
            change = total - option[1]
            print(f"You will receive {change} lei change.")
            print("Preparing your coffee...")
            time.sleep(3)
            print("Enjoy your coffee!")
            break
        else:
            print("The coffee machine accepts only bank-notes of 5 or 10 lei.")
else:
    print("This option doesn't exist")





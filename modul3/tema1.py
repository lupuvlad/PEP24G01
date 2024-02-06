import time

options = [["cappuccino", 4], ["espresso", 3.5]]

for i in range(len(options)):
    print(f"{i+1}. {options[i][0].title()}... {options[i][1]} lei")

coffee = input(f"Choose an option ({options[0][0]}/{options[1][0]}): ")

for option in options:
    if coffee == option[0]:
        pay = int(input("Insert only 5 or 10 lei: "))
        if pay == 5 or pay == 10:
            change = pay - option[1]
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

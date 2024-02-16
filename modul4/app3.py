accounts = {}

for i in range(3):
    user = input(f"Enter the user of the PC {i+1}: ")
    pwd = input(f"Enter the password of the PC {i+1}: ")
    # Add the user and password to the dictionary
    accounts[user] = pwd


for key in accounts.keys():
    print(key, "->", accounts.get(key))



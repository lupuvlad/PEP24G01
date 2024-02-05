PC_pass = 7788

guess = int(input("Enter the password: "))

while guess != PC_pass:
    if len(str(guess)) == 4:
        print("Wrong password! Try again.")
        guess = int(input("Enter the password: "))
        if guess == PC_pass:
            print("Access granted")
            break
    else:
        guess = int(input("The password must contain exactly 4 digits. Try again: "))

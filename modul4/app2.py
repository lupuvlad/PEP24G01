def power():
    while True:
        n1 = input("Type a number or 'q' if you want to quit: ")
        if n1 != 'q':
            return int(n1) ** int(n1)
        else:
            break


print(power())

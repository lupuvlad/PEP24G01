def calculate_x_and_y():
    for i in range(10, 20):
        y = 3 * i
        x = (3 * (i ** 2)) - (4 * y) + 4
        print(f"""============= X = {i} ==================
Rezultatul functiei: {x}""")


print(calculate_x_and_y())

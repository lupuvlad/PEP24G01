objects = ["Table", 5, "Chair", 4.5, [5, 6, 7], 8]

for thing in objects:
    print(f"The type of the object {thing} is {type(thing).__name__}.")

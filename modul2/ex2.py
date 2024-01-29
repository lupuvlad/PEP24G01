# Calculate the area of a triangle using the formula
# A = (1/2) * bh
# where b = base and h = height

# Get user input for the base and height of the triangle
b = int(input("b = "))
h = int(input("h = "))

# Create a variable in which you will store the result of the formula
A = (1/2) * b * h
# where A = area of the triangle

# Print the type of the variable A
print(type(A))

# Print the result
print("Area =", A)

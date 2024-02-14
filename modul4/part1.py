# Functions

# def add_(x, y):
#     return x + y
#     # print(x) # will never execute
#
#
# result = add_(2, 6)
# print(result)
# # print(x) # x not available outside the function


# # Example 1: factorials
# def factorial(x):
#     fact = 1
#     for i in range(1, x+1):
#         fact *= i
#     return fact
#
#
# result = factorial(5)
# print(result)


# Example 2: Gauss sum
def gauss(x):
    # with for
    # gauss_sum = 0
    # for i in range(1, x+1):
    #     gauss_sum += i
    # return gauss_sum
    # one-line with return
    return (x * (x+1)) / 2


result = gauss(10)
print(result)

# Sum from 1/1 to 1/x
def sumafractii(x):
    suma = 0
    for i in range(1, x+1):
        suma += 1/i
    return suma


print(sumafractii(100))

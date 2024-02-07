# lists

# result = "5,10".split(",")
# print(type(result))
# print(result)
#
# # location in memory
# my_list = []
# print(my_list, "before append")
# print(id(my_list), "in memory")
# my_list.append(1)
# print(my_list, "after append")
# print(id(my_list), "in memory")
#
# # pop method
# my_list.pop(0)
# print(my_list, "after pop")
# print(id(my_list), "in memory")

# is keyword
# my_var1 = "test 1"
# print(id(my_var1))
# my_var2 = "test 1"
# print(id(my_var2))
# print(my_var1 is my_var2)
# print(my_var1 == my_var2)
#
# my_var1 = f"test 1 {10-9}".capitalize()
# print(id(my_var1))
# my_var2 = "Test 1 1"
# print(id(my_var2))
# print(my_var1 is my_var2)
# print(my_var1 == my_var2)

# for with lists

new_list = [1, "5", True, None, [1, 2, 3]]

for obj in new_list:
    print(obj)


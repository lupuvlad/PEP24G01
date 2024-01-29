str1 = 'hello world'
print(type(str1))
int1 = 100
print(type(int1))
none = None
print(type(none))

# Capitalize method
result = str1.capitalize()
print("Returned type:", type(result))

# Formatted string
str1 = 'hello{} world{} {}'
text = "I'm Vlad"
result = str1.format(",", "!", text)
print("Formatted string:", result)

# Center method
str1 = 'hello world'
result = str1.center(20, "#")
print("Centered string:", result)



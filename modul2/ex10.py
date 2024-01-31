# Check if the string from the user input is palindrome
word = input("Write a word: ")

print(f"Palindrome: {word == word[::-1]}")

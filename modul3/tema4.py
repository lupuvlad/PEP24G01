word = input("Enter a word: ")
count = 0

for letter in word:
    if word[0] == letter:
        count += 1

print(f"'{word[0]}' appears {count} times.")

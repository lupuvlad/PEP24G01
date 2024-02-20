# 2.
num_of_books = int(input("How many books do you want to add in your library? "))
library = []
keys = ("name", "author", "year")

for i in range(num_of_books):
    book_info = {}
    print(f"===== Book {i + 1} =====")

    for key in keys:
        book_info[key] = input(f"What is the {key} of the book? ")

    library.append(book_info)

print("Your books are: ")
for book in library:
    print(book)

# 3.
input_year = int(input("Type a publication year: "))

for book in library:
    if input_year < int(book["year"]):
        print(f"{book["name"]} was published after the {input_year}.")

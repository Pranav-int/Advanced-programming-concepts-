def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")

    file = open("books.txt", "a")

    file.write(book_id + "," + title + "," + author + ",Available\n")

    file.close()

    print("Book added.")


def search_book():
    book_id = input("Enter Book ID: ")

    file = open("books.txt", "r")

    found = False

    for line in file:
        data = line.strip().split(",")

        if data[0] == book_id:
            print("Book Found:", data)
            found = True

    file.close()

    if not found:
        print("Book not found.")


def issue_book():
    book_id = input("Enter Book ID: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Issued"

        file.write(",".join(data) + "\n")

    file.close()

    print("Book issued.")


def return_book():
    book_id = input("Enter Book ID: ")

    file = open("books.txt", "r")
    lines = file.readlines()
    file.close()

    file = open("books.txt", "w")

    for line in lines:
        data = line.strip().split(",")

        if data[0] == book_id:
            data[3] = "Available"

        file.write(",".join(data) + "\n")

    file.close()

    print("Book returned.")


def display_available():
    file = open("books.txt", "r")

    print("Available Books:")

    for line in file:
        data = line.strip().split(",")

        if data[3] == "Available":
            print(data)

    file.close()


# Example operations
add_book()
search_book()
issue_book()
return_book()
display_available()
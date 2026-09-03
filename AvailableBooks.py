books = {
    101: {"title": "Python Basics", "available": True},
    102: {"title": "Data Science", "available": True}
}
def add_book(book_id, title):
    books[book_id] = {"title": title, "available": True}
def issue_book(book_id):
    if book_id in books and books[book_id]["available"]:
        books[book_id]["available"] = False
        print("Book issued successfully")
    else:
        print("Book not available")
def return_book(book_id):
    if book_id in books:
        books[book_id]["available"] = True
        print("Book returned successfully")
    else:
        print("Book not found")
def search_book(title):
    for book in books.values():
        if book["title"].lower() == title.lower():
            print("Book found:", book["title"])
            return
    print("Book not found")
def display_books():
    print("Available Books:")
    for book_id, book in books.items():
        if book["available"]:
            print(book_id, "-", book["title"])



add_book(103, "Machine Learning")

issue_book(101)
return_book(101)

search_book("Python Basics")

display_books()

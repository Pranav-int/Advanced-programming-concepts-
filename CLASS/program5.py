# Q5. Create a class Book containing book_id, title, author, and price.
# Create objects for three books and display their information.

class Book:
    def __init__(self, book_id, title, author, price):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("Book ID:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)
        print("------------------------")


# Creating three book objects
b1 = Book(101, "Python Programming", "John Smith", 500)
b2 = Book(102, "Java Programming", "James Gosling", 600)
b3 = Book(103, "Data Structures", "Robert Lafore", 700)

# Display information
b1.display()
b2.display()
b3.display()
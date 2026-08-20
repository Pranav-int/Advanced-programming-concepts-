books = {
    101: "Python",
    102: "Java",
    103: "C++"
}

books[104] = "HTML"

id = int(input("Search book ID: "))

if id in books:
    print("Book:", books[id])
else:
    print("Book not found")

id = int(input("Remove book ID: "))

if id in books:
    del books[id]

print("All books:", books)
print("Total books:", len(books))
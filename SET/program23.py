available_books = {"Python", "Java", "C", "DBMS", "HTML"}
requested_books = {"Python", "DBMS", "JavaScript", "Java"}

available = available_books & requested_books

print("Requested books that are available:", available)
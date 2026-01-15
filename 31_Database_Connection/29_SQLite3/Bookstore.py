import sqlite3

con = sqlite3.connect('Bookstore.db')
cur = con.cursor()
cur.execute('PRAGMA foreign_keys = ON')
# This line turns ON foreign key support in SQLite.
# SQLite does NOT check foreign keys by default,
# so we must enable it manually to make FOREIGN KEY constraints work.

print("\n=== BOOKSTORE DATABASE ===\n")

print("\n---------------------\n")

# create AUTHORS table
cur.execute("""
        CREATE TABLE IF NOT EXISTS AUTHOR(
            AUTHOR_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            AUTHOR_NAME TEXT NOT NULL,
            AUTHOR_EMAIL TEXT UNIQUE
        )
""")
con.commit()
print("AUTHORS table created sucsuessfully...")

# cur.execute("""
#         INSERT INTO AUTHOR (AUTHOR_NAME, AUTHOR_EMAIL) VALUES
#             ('J.K. Rowling', 'jkrowling@example.com'),
#             ('George R.R. Martin', 'grrmartin@example.com'),
#             ('J.R.R. Tolkien', 'jrrtolkien@example.com'),
#             ('Agatha Christie', 'achristie@example.com'),
#             ('Stephen King', 'sking@example.com'),
#             ('Dan Brown', 'dbrown@example.com')
# """)
# con.commit()
print("AUTHOR table data inserted successfully...")

print("\n---------------------\n")
# creat BOOKS table
cur.execute("""
        CREATE TABLE IF NOT EXISTS BOOKS (
            BOOK_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            BOOK_TITLE TEXT NOT NULL,
            AUTHOR_ID INTEGER NOT NULL,
            BOOK_PRICE REAL NOT NULL,  
            BOOK_STOCK INTEGER DEFAULT 0,
            FOREIGN KEY(AUTHOR_ID) REFERENCES AUTHOR(AUTHOR_ID)
        )
""")
con.commit()
print("BOOKS table created sucsuessfully...")

# cur.execute("""
#         INSERT INTO BOOKS (BOOK_TITLE, AUTHOR_ID, BOOK_PRICE, BOOK_STOCK) VALUES
#             ('Harry Potter and the Philosophers Stone', 1, 15.99, 50),
#             ('A Game of Thrones', 2, 20.50, 35),
#             ('The Hobbit', 3, 12.75, 40),
#             ('Murder on the Orient Express', 4, 10.99, 25),
#             ('The Shining', 5, 18.00, 30),
#             ('The Da Vinci Code', 6, 22.50, 45),
#             ('Harry Potter and the Chamber of Secrets', 1, 16.50, 40),
#             ('A Clash of Kings', 2, 21.00, 20)
# """)
# con.commit()
print("BOOKS table data inserted successfully...")

print("\n---------------------\n")

# Update a book’s price.
cur.execute("""
        UPDATE BOOKS SET BOOK_PRICE = 150.00 WHERE BOOK_TITLE = 'Harry Potter and the Philosophers Stone'
""")
con.commit()
print("Harry Potter and the Philosophers Stone Price Updated...")

print("\n---------------------\n")

# Update an author’s email.
cur.execute("""
        UPDATE AUTHOR SET AUTHOR_EMAIL = 'drashti@gmail.com' WHERE AUTHOR_ID = 2
""")
con.commit()
print("George R.R. Martin EMAIL address change...")

print("\n---------------------\n")

# # Delete a book with stock = 0.
# cur.execute("""
#         DELETE FROM BOOKS WHERE BOOK_STOCK = 0.00
# """)
# print("BOOKS with 0 stock deleted...")

# print("\n---------------------\n")

# # Delete an author with no books.
# cur.execute("""
#         DELETE FROM AUTHOR WHERE AUTHOR_ID NOT IN (
#             SELECT AUTHOR_ID FROM BOOKS) 
# """)
# con.commit()
# print("AUTHOR with no books deleted...")

# print("\n---------------------\n")

# INNER JOIN    List book title + author name for all books with valid authors.
cur.execute("""
        SELECT BOOKS.BOOK_TITLE, AUTHOR.AUTHOR_NAME FROM AUTHOR
            INNER JOIN BOOKS ON AUTHOR.AUTHOR_ID = BOOKS.AUTHOR_ID
""")
con.commit()
row = cur.fetchall()
print("Books with there author name...")
for title, name in row:
    print(f" - {title}, {name}")

print("\n---------------------\n")

# LEFT JOIN   List all books and their authors (even if author is NULL).
cur.execute("""
        SELECT BOOKS.BOOK_TITLE, AUTHOR.AUTHOR_NAME FROM BOOKS
            LEFT JOIN AUTHOR ON BOOKS.AUTHOR_ID = AUTHOR.AUTHOR_ID
""")
con.commit()
row = cur.fetchall()
print("All BOOKS and their authors...")
for title, name in row:
    print(f" - {title}, {name}")

print("\n---------------------\n")

# ORDER BY    List books in descending order of price.
cur.execute("""
        SELECT * FROM BOOKS ORDER BY BOOK_Price DESC
""")
con.commit()
row = cur.fetchall()
print("All Books using price descending order: ")
for book_id, title, author_id, price, stock in row:
    print(f" - {book_id}  {title}  {author_id}  {price}  {stock}")



print("\n---------------------\n")

# ORDER BY    List authors in alphabetical order.
cur.execute("""
        SELECT * FROM AUTHOR ORDER BY AUTHOR_NAME ASC
""")
con.commit()
row = cur.fetchall()
print("All Authors in alphabetical order: ")
for author_id, name, email in row:
    print(f" - {author_id}  {name}  {email}")

print("\n---------------------\n")

# LIMIT     List top 3 most expensive books.
cur.execute("""
        SELECT * FROM BOOKS ORDER BY BOOK_PRICE DESC LIMIT 3
""")
con.commit()
row = cur.fetchall()
print("List top 3 most expensive books: ")
for book_id, title, author_id, price, stock in row:
    print(f" - {book_id}  {title}  {author_id}  {price}  {stock}")

print("\n---------------------\n")

# # UNIQUE: try inserting duplicate email.
# cur.execute("""
#         INSERT INTO AUTHOR (AUTHOR_NAME, AUTHOR_EMAIL) VALUES
#             ('J.K. Rowling', 'drashti@example.com')
# """)
# con.commit()

# # FOREIGN KEY: try inserting a book with an invalid author_id.
# cur.execute("""
#         INSERT INTO BOOKS (BOOK_TITLE, AUTHOR_ID, BOOK_PRICE, BOOK_STOCK) VALUES
#             ('Harry Potter and the Philosophers Stone', 999, 15.99, 50)
# """)
# con.commit()



con.close()

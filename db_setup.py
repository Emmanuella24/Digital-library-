import sqlite3

conn = sqlite3.connect('library.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS users  (
        user_id integer PRIMARY KEY NOT NULL,
        first_name text,
        last_name text,
        social integer,
        email text
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS books  (
        name text,
        author text,
        category text,
        isbn integer PRIMARY KEY NOT NULL
        )""")

c.execute("""CREATE TABLE IF NOT EXISTS loans  (
        loan_id integer PRIMARY KEY NOT NULL,
        return_date text,
        library_id integer
        loaned BOOLEAN,
        loan_date text,
        isbn integer,   
        due_back text,
        )""")


print(c.fetchall())

conn.commit()
conn.close()
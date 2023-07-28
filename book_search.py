import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()


def book_search(isbn):

    result_dict = {}
    with conn:
        book_found = c.execute("SELECT isbn from books WHERE isbn=:isbn",
                            {'isbn': isbn})
        book_found = c.fetchone()
        if book_found:

            return book_found[0]


if __name__ == '__main__':
    book_search()
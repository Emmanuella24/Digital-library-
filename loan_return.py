import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
from datetime import date
from loan_search_sql import loan_search
from overdue_check import overdue_check


def loan_return():

    isbn = int(input("Enter the book isbn to return: "))
    overdue = overdue_check(isbn)
    if overdue == 'no':

        return_date = date.today()
        loaned = 0

        with conn:
            c.execute("""UPDATE loans SET loaned=?, return_date=? WHERE isbn=?""",
                      (loaned, return_date, isbn, ))

            conn.commit()
            print(c.rowcount)
            if c.rowcount > 0:
                print("Book returned, isbn {}".format(isbn))


if __name__ == '__main__':
    loan_return()
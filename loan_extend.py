import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
from datetime import timedelta, date
from overdue_check import overdue_check


def loan_extend():

    isbn = int(input("Enter the book isbn to extend: "))
    overdue = overdue_check(isbn)

    if overdue == 'no':

        today = date.today()
        due_date = today + timedelta(days=14)

        with conn:
            c.execute("""UPDATE loans SET due_date=? WHERE isbn=?""",
                      (due_date, isbn,))

            conn.commit()
            print(c.rowcount)
            if c.rowcount > 0:
                print("Loan Extended for book isbn: {} until: {}".format(isbn, due_date))

    else:
        print("Book isbn: {} is already overdue, cannot extend loan".format(isbn))


if __name__ == '__main__':
    loan_extend()
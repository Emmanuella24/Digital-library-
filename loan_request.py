import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
from datetime import timedelta, date


def loan_request(isbn):

    library_id = int(input("Please enter the user id of the loanee: "))
    loan_date = date.today()
    due_date = loan_date + timedelta(days=14)

    with conn:
        c.execute("""INSERT into loans ( library_id, loaned, loan_date, isbn, due_date) VALUES
                    (?, ?, ?, ?, ? )""", (library_id, 1, loan_date, isbn, due_date ))

        conn.commit()
        print(c.lastrowid)
    return c.lastrowid


if __name__ == '__main__':
    loan_request()
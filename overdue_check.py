import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()
from datetime import date
from loan_search_sql import loan_search


def overdue_check(isbn):

    loaned_tup = loan_search(isbn)
    loaned = loaned_tup[0]
    due_date = loaned_tup[1]
    return_date = date.today()
    return_date = str(return_date)

    if return_date > due_date:
        print("Book overdue, fine due.")
        overdue = 'yes'

    else:
        overdue = 'no'

    return overdue


if __name__ == '__main__':
    overdue_check()
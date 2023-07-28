import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()


def loan_search(isbn):

    result_dict = {}
    with conn:
        loan_found = c.execute(" SELECT loaned, due_date from loans WHERE isbn =:isbn ",
                               {'isbn': isbn})

        loan_found = c.fetchone()
#        loan_found = loan_found[0]
        print(loan_found)

    return loan_found


if __name__ == '__main__':
    loan_search()
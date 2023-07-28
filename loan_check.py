from book_search import book_search
from loan_search_sql import loan_search
from loan_request import loan_request


def book_check():

    loop = 'yes'
    while True and loop == 'yes':
        isbn = input("Please enter the isbn of the book you want to loan: ")
        if isbn:
            book_found = book_search(isbn)
            if book_found:
                loop = 'no'
                print("Book check: Book found: ")
                loan_check(book_found)
            else:
                print("Book not found")


def loan_check(book_found):

    isbn = book_found
    loaned_tup = loan_search(isbn)
    loaned = loaned_tup[0]
    due_date = loaned_tup[1]

    if loaned is None or loaned == 0:

        print("You can loan this book")
        loan_request(isbn)
    else:
        print("""This book is out on loan, due to be returned {}""".format(due_date))


if __name__ == '__main__':
    book_check()


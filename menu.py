from loan_request import loan_request
from loan_check import book_check
from loan_return import loan_return
from loan_extend import loan_extend
from users_add import add_user
from users_update import update_user
from book_add import book_add


def selection_validate():

    valid_selections = ('1', '2', '3', '4', '5', '6')
    message = input("Welcome to the main menu. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':

        selection = input("\nPlease select from the following menu (Type exit to exit program) \n"
                          "To request a new loan enter 1 \n"
                          "To return a book enter 2 \n"
                          "To extend a loan enter 3 \n"
                          "To add a user enter 4 \n"
                          "To update a user enter 5 \n"
                          "To add a book enter 6 \n"
                          "\nEnter choice: ")
        if selection == 'exit':
            break
        else:
            if selection in valid_selections:
                loop = 'no'

            else:
                print('\nValue: {} did not match any menu choice'.format(selection))
                loop = 'yes'
    return selection


def selection_calls():

    selection = selection_validate()

    if selection == '1':
        book_check()

    elif selection == '2':
        loan_return()

    elif selection == '3':
        loan_extend()

    elif selection == '4':
        add_user()

    elif selection == '5':
        update_user()

    elif selection == '6':
        book_add()


if __name__ == '__main__':
    selection_calls()
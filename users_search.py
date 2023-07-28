import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()


def find_user(user_id):

#    user_id = input("Enter the user id: ")
    account_found = {}
    with conn:
        c.execute("SELECT * from users WHERE user_id=:user_id",
                        {'user_id': user_id})

        account_found = c.fetchone()
        if account_found is None:
            print("There is no user matching user id: {} ".format(user_id))
        else:
            print("First Name: {}, Last Name: {}, Social: {}, Email: {}".format(account_found[1], account_found[2],
                                                                                account_found[3], account_found[4]))
    return account_found


if __name__ == '__main__':
    find_user()
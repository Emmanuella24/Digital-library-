import sqlite3
from users_search import find_user
conn = sqlite3.connect('library.db')
c = conn.cursor()


def update_user():
    library_id = input("Please enter the library id for the user you "
                       "want to modify: ")
    updates = {}

    with conn:
        account_found = find_user(library_id)

        if account_found:
            user_id = account_found[0]
            user_id = int(user_id)
            info = input("For each field enter the new data or enter n to make no change. Press y to proceed: ")
            first_name = input("Please enter the new first name or n: ")
            fields = ''
            if first_name != 'n' and first_name:
                updates['first_name'] = '?'
                fields = 'first_name'

            last_name = input("Please enter the last name or n: ")
            if last_name != 'n' and last_name:
                updates['last_name'] = '?'
                if fields:
                    fields = fields + ', ' + 'last_name'
                else:
                    fields = 'last_name'

            social = input("Please enter the social number or n: ")
            if social != 'n' and social:
                social = int(social)
                updates['social'] = '?'
                if fields:
                    fields = "{}, {}".format(fields, 'social')
                else:
                    fields = 'social'
            email = input("Please enter the email or n: ")
            if email != 'n' and email:
                updates['email'] = '?'
                if fields:
                    fields = fields + ', ' + 'email'
                else:
                    fields = fields + 'email'
            fields = "{}, {} ".format(fields, 'user_id')
            sql_fields = '(' + fields + ')'
            sql_tup = eval(sql_fields)
            updates = str(updates)
            updates = updates.replace("'", '').replace(":", '=').replace(":", '=').replace("{", '').replace("}", '')
            sql_first = 'UPDATE users SET'
            sql_middle = updates
            sql_last = 'WHERE user_id=?'
            sql_first_half = '{} {} {}'.format(sql_first, sql_middle, sql_last)
            c.execute(sql_first_half, sql_tup)
            conn.commit()
            if c.rowcount < 1:
                print("SQL user record update failed")
            else:
                print("User record updated")


if __name__ == '__main__':
    update_user()

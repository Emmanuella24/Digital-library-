import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()


def add_user():

    while True:
        first_name = input("Please enter the first name: ")
        if first_name:
            while first_name:
                last_name = input("Please enter the last name: ")
                if last_name:
                    while last_name:
                        social = input("Please enter the 9 digit social number. No dashes : ")
                        if social and social.isdigit() and len(social) == 9:
                            while social:
                                email = input("Please enter the email address: ")
                                if email:
                                    with conn:
                                        c.execute("INSERT into users (first_name, last_name, social, email) VALUES (?,?,?,?)",
                                                  (first_name, last_name, social, email))

                                        conn.commit()
                                        print("New library user has been added. library id: {} ".format(c.lastrowid))
                                    return c.lastrowid


if __name__ == '__main__':
    add_user()
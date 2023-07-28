import sqlite3
conn = sqlite3.connect('library.db')
c = conn.cursor()


def book_add():

    info = input("Please enter the book details at the prompts or type exit at any time to "
                 "exit the program. Press enter to continue: ")
    loop = 'yes'
    while True and loop == 'yes':

        name = input("Please enter the book title: ")
        if name == 'exit':
            break
        else:
            while name:

                author = input("Please enter the book author: ")
                if author == 'exit':
                    loop = 'no'
                    break
                else:
                    while author:

                        category = input("Please enter the book category: ")
                        while category:
                            if category == 'exit':
                                loop = 'no'
                                return
                            else:
                                loop = 'no'
                                with conn:
                                    c.execute("INSERT into books (name, author, category) VALUES (?,?,?)",
                                       (name, author, category))

                                    conn.commit()
                                    print("New book has been added. isbn is: {} ".format(c.lastrowid))
                                return c.lastrowid


if __name__ == '__main__':
    book_add()
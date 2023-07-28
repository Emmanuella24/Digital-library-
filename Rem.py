from tkinter import *
from tkinter import messagebox
import sqlite3
from sqlite3 import Error
#creating widow
class Rem(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(400, 200)
        self.minsize(400, 200)
        self.title("Remove User")
        self.canvas = Canvas(width=1366, height=768)
        self.canvas.pack()
        a = StringVar()
        def ent():
            d = messagebox.askyesno("Confirm", "Are you sure you want to remove the user?")
            if d:
                try:
                    self.conn = sqlite3.connect('library_administration.db')
                    self.myCursor = self.conn.cursor()
                    print(a.get())
                    self.myCursor.execute("Delete from admin where id = ?",[a.get()])
                    temp = self.myCursor.fetchone()
                    if temp:
                        messagebox.showinfo("Oop's","User Not Found")
                        a.set("")
                    else:
                        self.conn.commit()
                        self.myCursor.close()
                        self.conn.close()
                        messagebox.showinfo("Confirm","User Removed Successfully")
                        a.set("")
                except:
                    messagebox.showerror("Error","Something goes wrong")
        Label(self, text = "Username: ",bg='black',fg='white',font=('Arial', 15, 'bold')).place(x = 20,y = 40)
        Entry(self,textvariable = a,width = 37).place(x = 160,y = 44)
        Button(self, text='Remove', width=15, font=('arial', 10),command = ent).place(x=200, y = 90)



Rem().mainloop()

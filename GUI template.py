import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import font as tkfont

class EmotrikaApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family="Copperplate Gothic Bold",size=20)
        self.title("Emotrika")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=10)
        container.grid_columnconfigure(1, weight=10)
        container.grid_columnconfigure(1, minsize=100)
        self.geometry("%dx%d+%d+%d" % (800, 500, 500, 200))

        self.frames = {}
        for F in(StartScreen,LoginScreen, SignupScreen,MainScreen):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name]=frame
            frame.grid(row=0, column=1, sticky="nsew")
            frame.config(bg="white")

        self.show_frame("StartScreen")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class database():
    def create_table():
        dbcon = sqlite3.connect("database.db")
        dbcon.execute("CREATE TABLE IF NOT EXISTS logins(user_name text,user_pass text)")
        dbcon.commit()

    def insert_user():
        dbcon = sqlite3.connect("database.db")
        dbcon.execute("INSERT INTO logins(user_name, user_pass) VALUES(?,?)",(userName2, passWord2))
        dbcon.commit()

class StartScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Welcome to my app", font=controller.title_font)
        label1.grid(row=0)

        button1 =tk.Button(self, text="Let's Go",
                             command=lambda: controller.show_frame("SignUpScreen"))
        button1.grid(row=3)
        
class LoginScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="Login", font=controller.title_font)
        label1.pack()

        label2 = tk.Label(self, text="Username")
        label2.pack()
        global userName
        userName = Entry(self)
        userName.pack()
        
        label3 = tk.Label(self, text="Password")
        label3.pack()
        global passWord 
        passWord = Entry(self)
        passWord.pack()

        button3 = tk.Button(self, text="Accept",
                            command=lambda: controller.show_frame("MainScreen"))
        button3.pack()
        
        button1 =tk.Button(self, text="Start page",
                             command=lambda: controller.show_frame("StartScreen"))
        button1.pack(side="top", pady=2,padx=5)
        
        button2 =tk.Button(self, text="Sign Up",
                             command=lambda: controller.show_frame("SignupScreen"))
        button2.pack(side="top", pady=2, padx=5)
        
class SignupScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        def sign_check(event=None):
                global userName2, passWord2
                userName2 = userName.get()
                passWord2 = passWord.get()
                if not userName2 or not passWord2:
                    print(userName2)
                else:
                    create_table()
                    ("Username: %s Password: %s" % (userName.get(), passWord.get()))
                    insert_user()
                    controller.show_frame("LoginScreen")
                    
        label1 = tk.Label(self, text="Create your account!", font=controller.title_font)
        label1.pack()

        label2 = tk.Label(self, text="Username", font=(16))
        label2.pack()
        userName = Entry(self, text="Enter username", font=(14), bg="light grey")
        userName.pack()
        userName.bind("<Button-1>", clear_search)
        
        label3 = tk.Label(self, text="Password", font=(16))
        label3.pack()
        passWord = Entry(self, text="Enter Password", font=(14), bg="light grey", fg="black")
        passWord.pack()
        passWord.bind("<Button-1>", clear_search)

        button3 = tk.Button(self, text="Accept", command=sign_check)
        button3.pack()

        button2 =tk.Button(self, text="Already have an account? Login here!",
                             command=lambda: controller.show_frame("LoginScreen"))
        button2.pack(side="top", pady=2,padx=5)

class MainScreen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label1 = tk.Label(self, text="This is the Main Screen", font=controller.title_font)
        label1.pack()
    
if __name__ =="__main__":
    app = EmotrikaApp()
    app.mainloop()

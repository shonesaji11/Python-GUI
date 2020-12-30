try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2

import os
from pathlib import Path

global current_user
current_user = ""


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='monospace', size=18, weight="bold")  # , slant="italic"

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, Register, LoginSuccess, IncorrectPassword , UserRegistered, InvalidUser, UsernameChosen):   #ADD ALL NEW FRAMES INSIDE THIS TUPLE !!
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        print(self.frames)

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Budget App", bg="gray", width="300", height="2",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=0)

        button1 = tk.Button(self, text="Login", width=10,
                            command=lambda: controller.show_frame("PageOne"), font="monospace")
        button2 = tk.Button(self, text="Register", width=10,
                            command=lambda: controller.show_frame("Register"), font="monospace")
        '''button3 = tk.Button(self, text="Go to Page Three",width = 10,
                            command=lambda: controller.show_frame("PageThree"))'''
        button1.pack(padx=10, pady=(40, 0))
        button2.pack(padx=10, pady=(10, 0))
        #button3.pack(padx = 30 , pady=(10,0))


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=(10, 0))

        self.username_verify = ""
        self.password_verify = ""

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()

        self.username_login_entry = ""
        self.password_login_entry = ""

        tk.Label(self, text="Username : ").place(x=30, y=60)
        self.username_login_entry = tk.Entry(
            self, textvariable=self.username_verify)
        self.username_login_entry.place(x=150, y=60)

        tk.Label(self, text="Password  : ").place(x=30, y=90)
        self.password_login_entry = tk.Entry(
            self, textvariable=self.password_verify, show='*')
        self.password_login_entry.place(x=150, y=90)
        

        tk.Button(self, text="Login", width=15,
                  height=1, command=self.login_verify).pack(padx=(50, 50), pady=(110, 0))

        '''tk.Button(self, text="Login", width=10,
           height=1, command=lambda: controller.show_frame("PageTwo")).pack()'''

        button = tk.Button(self, text="Go to the start page",height=1,width = 15,
                           command=lambda: controller.show_frame("StartPage"))
        #tk.Label(text="  ").pack()
        button.pack(pady=(5, 0))
        


    def login_verify(self):
        print("entered")
        print(self.username_verify.get() , "username" , type(self.username_verify.get()))
        print(self.password_verify.get())

        users = {}
        filename = "users.txt"

        num_lines = sum(1 for line in open(filename))

        from itertools import islice
        for i in range(0, num_lines, 2):
            with open(filename, 'r') as infile:
                lines = [line for line in infile][i:i*2 + 2]
                users[lines[0][:-1]] = lines[1][:-1]

        try:
            password = users[str(self.username_verify.get())]
            if(password == self.password_verify.get() ):
                self.username_login_entry.delete(0 , tk.END)
                self.password_login_entry.delete(0 , tk.END)
                self.controller.show_frame("LoginSuccess")

            elif (self.username_verify.get() != ""):
                 self.controller.show_frame("PageOne")

            else:
                # wrong password
                print("wrong password")
                self.username_login_entry.delete(0 , tk.END)
                self.password_login_entry.delete(0 , tk.END)
                self.controller.show_frame("IncorrectPassword")

        except:
            print("Invalid User !!")
            # Display UNsuccessfully logged in page!!
            print(False)

            if(self.username_verify.get() == ""):
                self.controller.show_frame("PageOne")

            else:
                self.username_login_entry.delete(0 , tk.END)
                self.password_login_entry.delete(0 , tk.END)
                self.controller.show_frame("InvalidUser")


class InvalidUser(tk.Frame):


    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=(10, 0))

        self.username_verify = ""
        self.password_verify = ""

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()

        self.username_login_entry = ""
        self.password_login_entry = ""

        tk.Label(self, text="Username : ").place(x=30, y=60)
        self.username_login_entry = tk.Entry(
            self, textvariable=self.username_verify)
        self.username_login_entry.place(x=150, y=60)

        tk.Label(self, text="Password  : ").place(x=30, y=90)
        self.password_login_entry = tk.Entry(
            self, textvariable=self.password_verify, show='*')
        self.password_login_entry.place(x=150, y=90)

        tk.Label(self, text="Invalid User !! Try Again or Register ",
                 foreground="red").place(x = 80,y=120)

        tk.Button(self, text="Login", width = 15,
                  height=1, command=self.login_verify).pack(padx=(50, 50), pady=(110, 0))

        '''tk.Button(self, text="Login", width=10,
           height=1, command=lambda: controller.show_frame("PageTwo")).pack()'''

        button = tk.Button(self, text="Go to the start page",height=1,width = 15,
                           command=lambda: controller.show_frame("StartPage"))
        #tk.Label(text="  ").pack()
        button.pack(pady=(5, 0))

        button1 = tk.Button(self, text="Register",height=1,width = 15,
                    command=lambda: controller.show_frame("Register"))
        button1.pack(pady=(5, 0))

    def login_verify(self):
        print("entered")
        print(self.username_verify.get())
        print(self.password_verify.get())

        users = {}
        filename = "users.txt"

        num_lines = sum(1 for line in open(filename))

        from itertools import islice
        for i in range(0, num_lines, 2):
            with open(filename, 'r') as infile:
                lines = [line for line in infile][i:i*2 + 2]
                users[lines[0][:-1]] = lines[1][:-1]

        try:
            password = users[str(self.username_verify.get())]
            #if(password == self.password_verify.get() and username in users.keys()):
            if(password == self.password_verify.get() and self.username_verify.get() != ""):
                self.username_login_entry.delete(0 , tk.END)
                self.password_login_entry.delete(0 , tk.END)
                self.controller.show_frame("LoginSuccess")
            else:
                # wrong password
                print("wrong password")
                self.username_login_entry.delete(0 , tk.END)
                self.password_login_entry.delete(0 , tk.END)
                self.controller.show_frame("IncorrectPassword")
        except:
            print("Invalid User !!")
            # Display UNsuccessfully logged in page!!
            print(False)
            self.username_login_entry.delete(0 , tk.END)
            self.password_login_entry.delete(0 , tk.END)
            self.controller.show_frame("InvalidUser")



class Register(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Register",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        w = tk.Label(self, text="Username : ")
        w.place(x=40, y=70)

        w = tk.Label(self, text="Password  : ")
        w.place(x=40, y=100)

        self.username_verify = ""
        self.password_verify = ""

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()

        self.username_login_entry = ""
        self.password_login_entry = ""


        self.username_login_entry = tk.Entry(
            self, textvariable=self.username_verify)
        self.username_login_entry.place(x=155, y=70)

        self.password_login_entry = tk.Entry(
            self, textvariable=self.password_verify , show='*')
        self.password_login_entry.place(x=155, y=100)

        button = tk.Button(self, text="Register",width = 15, height = 1,
                           command=self.RegisterUser)
        #tk.Label(text="  ").pack()
        button.pack(pady=(95, 0))

        button = tk.Button(self, text="Go to the start page",width = 15, height = 1,
                           command=lambda: controller.show_frame("StartPage"))
        #tk.Label(text="  ").pack()
        button.pack(pady=(5, 0))
    
    def RegisterUser(self):
        my_file = Path("users.txt")
        if not my_file.is_file():
            f= open("users.txt","w+") #creates a new file if not present in the directory

        users = {}
        filename = "users.txt"

        num_lines = sum(1 for line in open(filename))

        if(num_lines > 1):
            from itertools import islice
            for i in range(0, num_lines, 2):
                with open(filename, 'r') as infile:
                    lines = [line for line in infile][i:i*2 + 2]
                    users[lines[0][:-1]] = lines[1][:-1]

        usernames = users.keys()

        if (str(self.username_verify.get()) not in usernames and self.username_verify.get() != ""):
            f= open("users.txt","a")
            f.write(self.username_verify.get() + "\n")
            f.write(self.password_verify.get() + "\n")
            f.close()
            print(f'{self.username_verify.get()} is registered')

            self.username_login_entry.delete(0 , tk.END)
            self.password_login_entry.delete(0 , tk.END)

            self.controller.show_frame("UserRegistered")
        else:
            print("Username already chosen !!")
            self.controller.show_frame("UsernameChosen")


    
class UsernameChosen(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Register",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        w = tk.Label(self, text="Username : ")
        w.place(x=40, y=70)

        w = tk.Label(self, text="Password  : ")
        w.place(x=40, y=100)

        self.username_verify = ""
        self.password_verify = ""

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()

        self.username_login_entry = ""
        self.password_login_entry = ""


        self.username_login_entry = tk.Entry(
            self, textvariable=self.username_verify)
        self.username_login_entry.place(x=155, y=70)

        self.password_login_entry = tk.Entry(
            self, textvariable=self.password_verify , show='*')
        self.password_login_entry.place(x=155, y=100)

        l = tk.Label(self, text="Username already chosen !! Please choose another username " ,  foreground="red") 
        l.place(x=10, y=140)

        button = tk.Button(self, text="Register", width = 15, height = 1,
                           command=self.RegisterUser)
        #tk.Label(text="  ").pack()
        button.pack(pady=(115, 0))

        button = tk.Button(self, text="Go to the start page",width = 15, height = 1, 
                           command=lambda: controller.show_frame("StartPage"))
        #tk.Label(text="  ").pack()
        button.pack(pady=(5, 0))

    def RegisterUser(self):
        my_file = Path("users.txt")
        if not my_file.is_file():
            f= open("users.txt","w+") #creates a new file if not present in the directory

        users = {}
        filename = "users.txt"

        num_lines = sum(1 for line in open(filename))

        if(num_lines > 1):
            from itertools import islice
            for i in range(0, num_lines, 2):
                with open(filename, 'r') as infile:
                    lines = [line for line in infile][i:i*2 + 2]
                    users[lines[0][:-1]] = lines[1][:-1]

        usernames = users.keys()

        if (str(self.username_verify.get()) not in usernames and self.username_verify.get() != ""):
            f= open("users.txt","a")
            f.write(self.username_verify.get() + "\n")
            f.write(self.password_verify.get() + "\n")
            f.close()
            print(f'{self.username_verify.get()} is registered')

            self.username_login_entry.delete(0 , tk.END)
            self.password_login_entry.delete(0 , tk.END)

            self.controller.show_frame("UserRegistered")
        else:
            print("Username already chosen !!")
            self.controller.show_frame("UsernameChosen")


        
class UserRegistered (tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Registration Successful",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


        


class IncorrectPassword(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Login",
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=(10, 0))

        self.username_verify = ""
        self.password_verify = ""

        self.username_verify = tk.StringVar()
        self.password_verify = tk.StringVar()

        self.username_login_entry = ""
        self.password_login_entry = ""

        tk.Label(self, text="Username : ").place(x=30, y=60)
        self.username_login_entry = tk.Entry(
            self, textvariable=self.username_verify)
        self.username_login_entry.place(x=150, y=60)

        tk.Label(self, text="Password  : ").place(x=30, y=90)
        self.password_login_entry = tk.Entry(
            self, textvariable=self.password_verify, show='*')
        self.password_login_entry.place(x=150, y=90)

        tk.Label(self, text="Incorrect Password !! Try Again ",
                 foreground="red").place(x = 80,y=120)

        tk.Button(self, text="Login", width=10,
                  height=1, command=self.login_verify).pack(padx=(50, 50), pady=(110, 0))


        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        #tk.Label(text="  ").pack()
        button.pack(pady=(5, 0))

    def login_verify(self):
        print("entered")
        print(self.username_verify.get())
        print(self.password_verify.get())

        users = {}
        filename = "users.txt"

        num_lines = sum(1 for line in open(filename))

        from itertools import islice
        for i in range(0, num_lines, 2):
            with open(filename, 'r') as infile:
                lines = [line for line in infile][i:i*2 + 2]
                users[lines[0][:-1]] = lines[1][:-1]

        try:
            password = users[str(self.username_verify.get())]
            #if(password == self.password_verify.get() and username in users.keys()):
            if(password == self.password_verify.get()):
                self.username_login_entry.delete(0 , tk.END)
                self.password_login_entry.delete(0 , tk.END)
                self.controller.show_frame("LoginSuccess")
            else:
                # wrong password
                print("wrong password")
                self.username_login_entry.delete(0 , tk.END)
                self.password_login_entry.delete(0 , tk.END)
                self.controller.show_frame("IncorrectPassword")
        except:
            print("Invalid User !!")
            # Display UNsuccessfully logged in page!!
            print(False)
            self.username_login_entry.delete(0 , tk.END)
            self.password_login_entry.delete(0 , tk.END)
            self.controller.show_frame("StartPage")


class LoginSuccess(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        s = f"Welcome to BudgetApp {current_user}"
        print("current_user", current_user)
        label = tk.Label(self, text=s,
                         font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.geometry("430x280")
    app.title("")
    app.mainloop()

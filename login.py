from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
import os # You need to import this module to launch another script

# Colors
co1 = "#525561"
co2 = "#FFFFFF"
co3 = "#1D90F5"

root = Tk()
root.title("Login")
root.geometry('400x450')
root.resizable(width=False, height=False)
root.configure(bg=co1)

frame_up = Frame(root, width=310, height=50, bg=co1)
frame_up.grid(row=0, column=0)

frame_down = Frame(root, width=310, height=400, bg=co1)
frame_down.grid(row=1, column=0)
heading = Label(frame_up, text="LOGIN", bg=co1, font=('yu gothic ui Bold', 23), fg=co2)
heading.place(x=80, y=5)


line = Label(frame_up, width=40, text="", height=1, bg=co3, anchor=NW)
line.place(x=10, y=45)
label_style = {"font": ('yu gothic ui Regular', 15), "fg": co2, "bg": co1, "anchor": NW}
username = Label(frame_down, text="username *", height=1, **label_style)

username.place(x=10, y=10)

e_name = Entry(frame_down, width=25, justify='left', font=("", 15), highlightthickness=1)
e_name.place(x=14, y=48)
password = Label(frame_down, text="password *", height=1, **label_style)
password.place(x=10, y=95)
e_password = Entry(frame_down, width=25, justify='left', show='*', font=("", 15), highlightthickness=1)

e_password.place(x=14, y=130)
email = Label(frame_down, text="email *", height=1, **label_style)
email.place(x=10, y=175)
e_email = Entry(frame_down, width=25, justify='left', font=("", 15), highlightthickness=1)

e_email.place(x=14, y=210)
email_password = Label(frame_down, text="email password *", height=1, **label_style)

email_password.place(x=10, y=255)

e_email_password = Entry(frame_down, width=25, justify='left', show='*', font=("", 15), highlightthickness=1)
e_email_password.place(x=14, y=290)

# Button

button_confirm = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font=("Ivy 9 bold"))
button_confirm.place(x=35, y=400)

# Credentials
credentials = [
  ['keerthi', 'keerthiv', 'keerthivasansv2006@gmail.com', 'keerthivasan'],
]

def check_password():
  name = e_name.get()
  password = str(e_password.get())
  email = e_email.get()
  email_password = e_email_password.get()

  for user in credentials:
    if name == user[0] and password == user[1] and email == user[2] and email_password == user[3]:
      messagebox.showinfo('Login', f'Welcome, {name}!')
      # Launch the my_firebase.py script
      os.system('python my_firebase.py')
      return # Exit the loop if a matching user is found

  messagebox.showwarning('Error', 'Invalid username, password, email, or email password')

button_confirm = Button(frame_down, text="Login", bg=co3, fg=co1, width=39, height=2, font=("Ivy 9 bold"), command=check_password)
button_confirm.place(x=15, y=335)

root.mainloop()
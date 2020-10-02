from tkinter import *
from tkinter import messagebox

tk = Tk()

def funk_ok():
    messagebox.showinfo('Thanks for entering!')
    print('Thanks for entering!')
    str_login = login_field.get()
    str_pass = pass_field.get()
    messagebox.showerror(f'Your login is {str_login}, password is {str_pass}')



tk.geometry('400x300')

#canv = Canvas(tk)

frame = Frame(tk, bg='red', relief=RIDGE, borderwidth=2)
frame.pack()

login_field = Entry(frame, bg='white')
login_field.pack()

pass_field = Entry(frame, bg='white', show='*')
pass_field.pack()

bt_send = Button(frame, bg='#fafafa', text='Enter!', command=funk_ok)
bt_send.pack()

                   
    
tk.mainloop()
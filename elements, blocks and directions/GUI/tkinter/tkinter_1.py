from tkinter import *

root = Tk()

# background?
root['bg'] = '#ffffff'

# title of window
root.title = 'Name of my program window'

# size of window
root.geometry('400x300')

# resizable
root.resizable(width=False, height=True)

# canvas
canvas = Canvas(root, height=280, width=380)
canvas.pack()

# frame
frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.6)

frame2 = Frame(frame, bg='blue')
frame2.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.25)


my_text = Label(frame, text='New text here!', bg='white')
my_text.place(rely=0.03, relx=0.05)
my_button = Button(frame2, text='This is a button', bg='grey')
my_button.place(rely=0.72, relx=0.05)

login_f = Entry(frame2, bg='white')
login_f.pack(anchor='center')



root.mainloop()
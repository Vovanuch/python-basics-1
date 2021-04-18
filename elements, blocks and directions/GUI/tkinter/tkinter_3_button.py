from tkinter import *

root = Tk()
root.title("GUI window with python")
root.geometry('300x250')

btn = Button(text = 'Hello!',
             background="#555",     # фоновый цвет кнопки
             foreground="#ccc",     # цвет текста
             padx="40",             # отступ от границ до содержимого по горизонтали
             pady="20",              # отступ от границ до содержимого по вертикали
             #font="16"              # высота шрифта
             )
btn.pack()

root.mainloop()
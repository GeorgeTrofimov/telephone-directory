from email import message
from tkinter import *
from tkinter import messagebox
from turtle import title  
root = Tk()

def btn_click():
    print('Some text')
#def btn_click():  
    last_name = last_name.get()
    first_name = first_name.get()
    phone_number = phone_number.get()
    
    info_str = f'Данные: {str(last_name)}, {str(first_name)}, {int(phone_number)}'
    messagebox.showinfo(title='Название', message=info_str)
root['bg'] = '#fafafa'
root.title('TemporaryDirectory')
root.wm_attributes('-alpha', 0,7)
root.geometry('600x400')

root.resizable(width=False, height=False)

Canvas = Canvas(root, height=600, width=400)
Canvas.pack()

frame = Frame(root, bg = 'red')
frame.place(relx=0.15, rely= 0.15, relwidth=0.7, relheight=0.7)

title = Label(frame, text='Текст подсказка', bg = 'grey', font=40)
title.pack()
btn = Button(frame, text='Кнопка', bg = 'yellow')
btn.pack()

last_name = Entry(frame, bg='white')
last_name.pack()

first_name = Entry(frame, bg='white')
first_name.pack()

phone_number = Entry(frame, bg='white')
phone_number.pack()

root.mainloop()

def view_data(data):
    print(data)
def last_name():
    return input('Введите фамилию: ')
def first_name():
    return input('Введите имя: ')
def phone_number():
    return input('Введите номер телефона: ')
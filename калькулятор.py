# создание калькулятора

import tkinter as tk
from tkinter import messagebox #для появления всплывающих окон с информацией

def add_digit(digit): #функция добавления цифр. используется в строке и при создании кнопок
    value = calc.get()
    if value[0]=='0' and len(value)==1: #по дефолту отображается 0 при введении любого символа 0 пропадает
      value = value[1:]
    calc['state'] = tk.NORMAL #добавляется при вводе цифр, символов, вывода результата.
    calc.delete(0, tk.END)
    calc.insert(0, value+digit)
    calc['state'] = tk.DISABLED #в остальное время поле ввода блокируется от введения ненужных символов

def add_operation(operation): #функция для создания операций
    value = calc.get()
    if value[-1] in '-+/*':
        value = value[:-1] #последней может быть только одна операция
    elif '+' in value or '-' in value or '*' in value or '/' in value: #если в строке уже есть значения к вычислению,
        #сначала производятся вычисления, потом продолжается запись выражения
        calculate()
        value = calc.get()

    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, value+operation)
    calc['state'] = tk.DISABLED


def calculate():
    value = calc.get()
    if value[-1] in '+-*/':
        value = value+value[:-1]
        calc.delete(0, tk.END)
    try:
        calc['state']=tk.NORMAL
        calc.delete(0, tk.END)
        calc.insert(0, eval(value))
        calc['state'] = tk.DISABLED
    except (NameError, SyntaxError): #в случае введения букв или служебных символов появляется окно с информацией
        messagebox.showinfo('Внимание', "Нужно вводить только цифры. Вы ввели другие символы!")
        calc.insert(0, 0)
    except ZeroDivisionError:
        messagebox.showinfo('Внимание', 'На ноль делить нельзя!!') #первая фразу уходит в заголовок, вторая внутрь окна
        calc.insert(0,0)

def clear():
    calc['state'] = tk.NORMAL
    calc.delete(0, tk.END)
    calc.insert(0, '0')
    calc['state'] = tk.DISABLED


def make_digit_buttom(digit):
    return tk.Button(win, text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))

def make_operation_buttom(operation):
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))

def make_calc_buttom(operation):
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate)

def make_clear_buttom(operation):
    return tk.Button(win, text=operation, bd=5, font=('Arial', 13), fg='red', command=clear)

def press_key(event):
    print(repr(event.char))
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '/*-+':
        add_operation(event.char)
    elif event.char == '\r':
        calc['state'] = tk.NORMAL
        calculate()
        calc['state'] = tk.DISABLED


win = tk.Tk()
win.geometry('240x270+100+100')
win['bg'] = '#33ffe6'
win.title('Калькулятор')

win.bind('<Key>', press_key)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=15)
calc.insert(0,'0')
calc['state'] = tk.DISABLED
calc.grid(row=0, column=0, columnspan=4, stick='we', padx=5)

make_digit_buttom('1').grid(row=1, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('2').grid(row=1, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('3').grid(row=1, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('4').grid(row=2, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('5').grid(row=2, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('6').grid(row=2, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('7').grid(row=3, column=0, stick='wens', padx=5, pady=5)
make_digit_buttom('8').grid(row=3, column=1, stick='wens', padx=5, pady=5)
make_digit_buttom('9').grid(row=3, column=2, stick='wens', padx=5, pady=5)
make_digit_buttom('0').grid(row=4, column=0, stick='wens', padx=5, pady=5)

make_operation_buttom('+').grid(row=1, column=3, stick='wens', padx=5, pady=5)
make_operation_buttom('-').grid(row=2, column=3, stick='wens', padx=5, pady=5)
make_operation_buttom('/').grid(row=3, column=3, stick='wens', padx=5, pady=5)
make_operation_buttom('*').grid(row=4, column=3, stick='wens', padx=5, pady=5)

make_calc_buttom('=').grid(row=4, column=2, stick='wens', padx=5, pady=5)
make_clear_buttom('c').grid(row=4, column=1, stick='wens', padx=5, pady=5)

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)

win.mainloop()

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk

import backend
from backend import process_data


# Функция для обработки нажатий клавиш
def process_input(c):
	c = c.lower()
	if c in '0123456789.-e':

		if main_label['text'] in ['Введите число в 10-ичной СС', 'Введите число в 9-ичной СС']:
			main_label['text'] = ''

		elif len(main_label['text']) >= 27:
			return

		main_label['text'] += c

	elif c == '\x08' and main_label['text'] not in \
	['Введите число в 10-ичной СС', 'Введите число в 9-ичной СС']:
		new_text = main_label['text'][:-1]

		if len(new_text) == 0:
			main_label['text'] = f'Введите число в {10 if backend.MODE == 109 else 9}-ичной СС'
		else:
			main_label['text'] = new_text


# Сменить направление перевода
def switch_mode():
	if mode_btn['text'] == '10 --> 9':
		mode_btn['text'] = '9 --> 10'
		main_label['text'] = 'Введите число в 9-ичной СС'
		backend.MODE = 910
	else:
		mode_btn['text'] = '10 --> 9'
		main_label['text'] = 'Введите число в 10-ичной СС'
		backend.MODE = 109


# Хэндлер для нажатий кнопок на клавиатуре
def onkeydown(e):
    process_input(e.char)


# Функция для подсчета выражения
def compute(e=''):
	num = main_label['text']
	status, result = process_data(num, backend.MODE)
	if len(result) > 27:
		print(result)
	else:
		sec_label['text'] = result


# Очистка поля ввода
def clear_input():
	main_label['text'] = 'Введите число в 10-ичной СС' \
	if backend.MODE == 109 else 'Введите число в 9-ичной СС'


# Очистка поля вывода
def clear_output():
	sec_label['text'] = 'Результат'


# Очистка всех полей
def clear():
	main_label['text'] = 'Введите число в 10-ичной СС' \
	if backend.MODE == 109 else 'Введите число в 9-ичной СС'
	sec_label['text'] = 'Результат'


def show_info():
	showinfo('Информация об авторе', 'Диваев Александр, ИУ7-22Б\nЛаба 1')
	

root = Tk()
root.geometry('512x350')
root.bind('<KeyPress>', onkeydown)
root.bind('<Return>', compute)
root.title('Converter')
root.resizable(False, False)
menubar = Menu(root)
root.config(menu=menubar)


action_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Действия', menu=action_menu)
action_menu.add_command(label='Перевод из одной СС в другую', command=compute)
action_menu.add_command(label='Поменять СС местами', command=switch_mode)
action_menu.add_command(label='Очистить поле ввода', command=clear_input)
action_menu.add_command(label='Очистить поле вывода', command=clear_output)
action_menu.add_command(label='Очистить все поля', command=clear)


info_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Информация', menu=info_menu)
info_menu.add_command(label='Информация об авторе', command=show_info)


frm = ttk.Frame(root, padding=10)
frm.grid()

main_label = ttk.Label(frm, text='Введите число в 10-ичной СС', font=('Helvetica', 24), 
	anchor='center', borderwidth=1, width=27, relief='solid')
main_label.grid(column=0, row=0, columnspan=15, padx=(1, 24))

sec_label = ttk.Label(frm, text='Результат', font=('Helvetica', 24), 
	anchor='center', borderwidth=1, width=27, relief='solid')
sec_label.grid(column=0, row=1, pady=10, columnspan=15, padx=(1, 24))

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 16))

ttk.Button(frm, text='7', width=4, style='my.TButton', 
	command=lambda m='7': process_input(m)).grid(column=0, row=2, ipady=10)
ttk.Button(frm, text='8', width=4, style='my.TButton', 
	command=lambda m='8': process_input(m)).grid(column=1, row=2, ipady=10)
ttk.Button(frm, text='9', width=4, style='my.TButton', 
	command=lambda m='9': process_input(m)).grid(column=2, row=2, ipady=10)

ttk.Button(frm, text='4', width=4, style='my.TButton', 
	command=lambda m='4': process_input(m)).grid(column=0, row=3, pady=3, ipady=10)
ttk.Button(frm, text='5', width=4, style='my.TButton', 
	command=lambda m='5': process_input(m)).grid(column=1, row=3, ipady=10)
ttk.Button(frm, text='6', width=4, style='my.TButton', 
	command=lambda m='6': process_input(m)).grid(column=2, row=3, ipady=10)

ttk.Button(frm, text='1', width=4, style='my.TButton', 
	command=lambda m='1': process_input(m)).grid(column=0, row=4, ipady=10)
ttk.Button(frm, text='2', width=4, style='my.TButton', 
	command=lambda m='2': process_input(m)).grid(column=1, row=4, ipady=10)
ttk.Button(frm, text='3', width=4, style='my.TButton', 
	command=lambda m='3': process_input(m)).grid(column=2, row=4, ipady=10)

ttk.Button(frm, text='-', width=4, style='my.TButton', 
	command=lambda m='-': process_input(m)).grid(column=0, row=5, pady=3, ipady=10)
ttk.Button(frm, text='0', width=4, style='my.TButton', 
	command=lambda m='0': process_input(m)).grid(column=1, row=5, ipady=10)
ttk.Button(frm, text='.', width=4, style='my.TButton', 
	command=lambda m='.': process_input(m)).grid(column=2, row=5, ipady=10)

ttk.Button(frm, text='Backspace', width=14, style='my.TButton', 
	command=lambda m='\x08': process_input(m)) \
	.grid(column=3, row=2, ipady=10, columnspan=5, padx=(8, 0))

mode_btn = ttk.Button(frm, text='10 --> 9', width=10, style='my.TButton', 
	command=switch_mode)
mode_btn.grid(column=10, row=2, ipady=10, columnspan=5, padx=(0, 23))

ttk.Button(frm, text='Конвертировать', width=25, style='my.TButton', 
	command=compute).grid(column=3, row=3, ipady=10, columnspan=8, padx=(8, 15))

ttk.Button(frm, text='Очистить все поля', width=25, style='my.TButton', 
	command=clear).grid(column=3, row=4, ipady=10, columnspan=8, padx=(8, 15))

ttk.Label(frm, text='Диваев Александр, ИУ7-22Б\nЛаба 1', justify='center', 
	font=('Helvetica', 16), anchor='center', borderwidth=1, width=25, relief='solid') \
	.grid(column=3, row=5, columnspan=16, rowspan=15, padx=(4, 16))



root.mainloop()

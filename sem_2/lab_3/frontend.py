import os

from tkinter import *
from tkinter import ttk, filedialog
from tkinter.messagebox import showinfo

from backend import encode, decode

LENGTH = 600
HEIGHT = 270
SYMBOL_WIDTH = 8
file_path = ['']


def get_file_path():
	filepath = filedialog.askopenfilename(title='Выбор файла',
				initialdir=os.getcwd(), filetypes=[('Bitmap pictures', '*.bmp')],
				initialfile='sample.bmp')

	if not filepath:
		return

	file_path[0] = filepath


def prepare_data_to_encode():
	message = text.get('1.0', END).strip()
	if not message:
		showinfo('Ошибка', 'Введите сообщение, которое необходимо закодировать.')
		return

	filepath = file_path[0]
	if not filepath:
		showinfo('Ошибка', 'Файл не выбран.')
		return

	file_path[0] = ''

	status, info = encode(filepath, message)
	if not status:
		showinfo('Ошибка', info)
	else:
		showinfo('Успех', 'Сообщение закодировано в файле encoded_image.bmp')


def prepare_data_to_decode():
	filepath = file_path[0]
	if not filepath:
		showinfo('Ошибка', 'Файл не выбран.')
		return

	file_path[0] = ''
	label['text'] = ''

	status, info = decode(filepath)
	if not status:
		showinfo('Ошибка', info)
		return

	label['text'] = info



root = Tk()
root.geometry(f'{LENGTH+3}x{HEIGHT}')
root.title('Steganography')
root.resizable(False, False)

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 16))
ls = ttk.Style()
ls.configure('Custom.TLabel', borderwidth=2, relief='solid')


ttk.Label(text='=' * (LENGTH // SYMBOL_WIDTH)).place(x=0, y=120)

ttk.Label(text='Закодировать (деда)',
		  justify='center', font=16).place(x=5, y=5)
ttk.Label(text='Сообщение', justify='center', font=16).place(x=350, y=5)
ttk.Button(text='Выбрать файл', style='my.TButton',
		   command=get_file_path, width=15).place(x=5, y=50)
ttk.Button(text='Закодировать', style='my.TButton',
		   command=prepare_data_to_encode, width=15).place(x=5, y=90)
text = Text(font=14, width=33, height=3)
text.place(x=220, y=50)

ttk.Label(text='Декодировать (деда)',
		  justify='center', font=16).place(x=5, y=140)
ttk.Label(text='Сообщение', justify='center', font=16).place(x=350, y=140)
ttk.Button(text='Выбрать файл', style='my.TButton',
		   command=get_file_path, width=15).place(x=5, y=185)
ttk.Button(text='Декодировать', style='my.TButton',
		   command=prepare_data_to_decode, width=15).place(x=5, y=225)
label = ttk.Label(justify='left', font=14, wraplength=365,
				  width=33, style='Custom.TLabel')
label.place(x=220, y=185)


root.mainloop()

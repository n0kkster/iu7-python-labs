from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import matplotlib.pyplot as plt

from backend import process_data, gen_plot_data, find_extremums, find_inflection_points


def create_entry(placeholder, _x, _y, _width=-1):

	def remove_placeholder(e):
		if entry.get() == placeholder:
			entry.delete(0, END)

	def set_placeholder(e):

		if entry.get() == '':
			entry.insert(0, placeholder)

	if _width == -1:
		_width = len(placeholder)

	entry = ttk.Entry(justify='center', font=16, width=_width)
	entry.insert(0, placeholder)
	entry.place(x=_x, y=_y)
	entry.bind('<FocusIn>', remove_placeholder)
	entry.bind('<FocusOut>', set_placeholder)

	return entry


def gen_table(data):
	table = ttk.Treeview(show='headings', columns=(
		'#1', '#2', '#3', '#4', '#5', '#6'))
	table.place(x=10, y=120, width=572, height=370)

	table.heading('#1', text='#', anchor=W)
	table.heading('#2', text='[x_i;x_i+1]', anchor=W)
	table.heading('#3', text='x\'', anchor=W)
	table.heading('#4', text='f(x\')', anchor=W)
	table.heading('#5', text='Число итераций', anchor=W)
	table.heading('#6', text='Код ошибки', anchor=W)

	table.column('#1', width=20)
	table.column('#2', width=80)
	table.column('#3', width=100)
	table.column('#4', width=140)
	table.column('#5', width=90)
	table.column('#6', width=70)

	for i in range(len(data)):
		data[i][1] = round(data[i][1], 6)
		line = tuple([i] + data[i])
		table.insert('', END, values=line)

	ysb = ttk.Scrollbar(orient=VERTICAL, command=table.yview)
	table.configure(yscroll=ysb.set)
	ysb.place(x=592, y=120, width=20, height=370)


def compute():
	try:
		func = func_entry.get()

		if '=' in func:
			func = func.split('=')[1]

		precision = float(precision_entry.get())

		if precision < 1e-15:
			raise

		start = float(start_entry.get())
		stop = float(stop_entry.get())
		step = float(step_entry.get())
		nmax = int(nmax_entry.get())
	except:
		showinfo('Ошибка', 'Данные введены неверно')
		return

	roots, status = process_data(func, precision, start, stop, step, nmax)
	print(roots)

	if not status[0]:
		showinfo('Ошибка', status[1])
		return

	gen_table(roots)

	plt.clf()
	plt.xlabel('X')
	plt.ylabel('Y')
	plt.title('График функции')
	plt.grid(True)
	plt.plot([r[1] for r in roots if not r[4]], [float(r[2])
				for r in roots if not r[4]], 'ro', label='Корень')

	x, y, status = gen_plot_data(func, start, stop)
	if not status[0]:
		showinfo('Ошибка', status[1])
		return
	plt.plot(x, y, label='Функция')

	roots, status = find_extremums(func, start, stop, step)
	if not status[0]:
		showinfo('Ошибка', status[1])
		return
	plt.plot([r[0] for r in roots], [float(r[1])
				for r in roots], 'go', label='Экстремум')

	roots, status = find_inflection_points(func, start, stop, step)
	if not status[0]:
		showinfo('Ошибка', status[1])
		return
	plt.plot([r[0] for r in roots], [float(r[1])
				for r in roots], 'bo', label='Точка перегиба')

	plt.legend()
	plt.show()


root = Tk()
root.geometry('612x500')
root.title('Roots')
root.resizable(False, False)

s = ttk.Style()
s.configure('my.TButton', font=('Helvetica', 16))

func_entry = create_entry('Функция в аналитическом виде', 10, 10)
step_entry = create_entry('Шаг деления', 330, 10)
precision_entry = create_entry('Точность eps', 462, 10)
start_entry = create_entry('Начало отрезка', 10, 45)
stop_entry = create_entry('Конец отрезка', 175, 45)
nmax_entry = create_entry('Макс. количество итераций', 330, 45, 24)
ttk.Button(text='Посчитать', width=41, style='my.TButton',
		   command=compute).place(x=60, y=80)


root.mainloop()

from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk
from itertools import combinations, permutations

# Основной класс со всеми действиями
class CircleDrawer:
	def __init__(self, master):

		# Инициалищируем окно
		self.master = master
		self.master.geometry('1000x600')
		self.master.title('Desmos 5D')
		self.master.resizable(False, False)
		self.s = ttk.Style()
		self.s.configure('my.TButton', font=('Helvetica', 16))

		self.WIDTH = 550
		self.HEIGHT = 550
		self.center = None
		self.dots = set()

		# Создаем канвас
		self.canvas = Canvas(master, width=self.WIDTH, height=self.HEIGHT, bg='white')
		self.canvas.place(x=425, y=25)

		# Хендлеры для обработки событий, связанных с канвасом
		self.canvas.bind("<Button-1>", self.on_click)

		# === Создаем ГУИ ===
		ttk.Label(text='X точки: ', font=('Helvetica', 16)).place(x=25, y=25)
		self.x_entry = ttk.Entry(font=('Helvetica', 16))
		self.x_entry.place(x=25, y=60)
		ttk.Label(text='Y точки: ', font=('Helvetica', 16)).place(x=25, y=125)
		self.y_entry = ttk.Entry(font=('Helvetica', 16))
		self.y_entry.place(x=25, y=160)
		
		self.draw_button = ttk.Button(text='Нарисовать', style='my.TButton', width=10, command=self.on_btn_pressed)
		self.draw_button.place(x=125, y=325)

		self.draw_button = ttk.Button(text='Посчитать', style='my.TButton', width=10, command=self.compute)
		self.draw_button.place(x=125, y=425)

		self.draw_button = ttk.Button(text='Очистить', style='my.TButton', width=10, command=self.clear_canvas)
		self.draw_button.place(x=125, y=525)
		# ===================

	# Основная функция для нахождения искомого четырехугольника
	def compute(self):
		n = len(self.dots)
		s = 0
		p = list(self.dots)
		maxsq = []
		for x, i in enumerate(p, 1):
			for j in p[x:]:
				a = b = 0
				sq = [None, None, None, None]
				sq[0] = i
				sq[1] = j
				for k in p:
					d = (i[0] - k[0]) * (j[1] - k[1]) - (i[1] - k[1]) * (j[0] - k[0])

					if d < a:
						a = d
						sq[2] = k

					if d > b:
						b = d
						sq[3] = k

				if a and b: 
					if s < b - a:
						s = b - a
						maxsq = sq

		for p in permutations(maxsq):
			sqd = []
			for d in p:
				sqd.append(d[0])
				sqd.append(d[1])
			self.canvas.create_polygon(sqd)



	# Обработка нажатия кнопки, отвечающей за рисование окружности
	def on_btn_pressed(self):
		try:
			# === Валидация данных ===
			x = float(self.x_entry.get())
			if x < 0 or x > 550:
				raise ValueError

			y = float(self.y_entry.get())
			if y < 0 or y > 550:
				raise ValueError
			# ========================

			# Проверка, что ввод на канвасе еще активен
			if self.center is not None:
				showinfo('Ошибка', 'Сначала закончите ввод на канвасе!')
				return

			# Рисуем точку
			self.center = (x, y)
			self.draw_circle()
			self.reset()

		except:
			showinfo('Ошибка', 'Данные введены неверно!')
			return

	# Обработка нажатия на канвас
	def on_click(self, event):
		self.center = (event.x, event.y)
		self.draw_circle()

	# Функция для рисования окружности
	def draw_circle(self):
		x0, y0 = self.center
		r = 1
		# Проверка, что окружность влезает на канвас
		if x0 - r < 0 or y0 - r < 0 or x0 + r > self.WIDTH or y0 + r > self.HEIGHT:
			return

		# Рисуем окружность
		self.canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, outline='blue')
		
		# При необходимости добавляем окружность в список окружностей
		self.dots.add(self.center)

	# Очистка канваса
	def clear_canvas(self):
		self.canvas.delete('all')
		self.dots = set()


root = Tk()
app = CircleDrawer(root)
root.mainloop()

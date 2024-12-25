from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk

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

		# Создаем канвас
		self.canvas = Canvas(master, width=self.WIDTH, height=self.HEIGHT, bg='white')
		self.canvas.place(x=425, y=25)

		# Переменные для работы с окружностями
		self.center = None
		self.radius = None
		self.circles = set()
		self.temp_circle = None

		# Хендлеры для обработки событий, связанных с канвасом
		self.canvas.bind("<Button-1>", self.on_click)
		self.canvas.bind("<Motion>", self.on_move)

		# === Создаем ГУИ ===
		ttk.Label(text='X центра окружности [0;550]: ', font=('Helvetica', 16)).place(x=25, y=25)
		self.x_entry = ttk.Entry(font=('Helvetica', 16))
		self.x_entry.place(x=25, y=60)
		ttk.Label(text='Y центра окружности [0;550]: ', font=('Helvetica', 16)).place(x=25, y=125)
		self.y_entry = ttk.Entry(font=('Helvetica', 16))
		self.y_entry.place(x=25, y=160)
		ttk.Label(text='Радиус окружности [0;550]: ', font=('Helvetica', 16)).place(x=25, y=225)
		self.radius_entry = ttk.Entry(font=('Helvetica', 16))
		self.radius_entry.place(x=25, y=260)
		
		self.draw_button = ttk.Button(text='Нарисовать', style='my.TButton', width=10, command=self.on_btn_pressed)
		self.draw_button.place(x=125, y=325)

		self.draw_button = ttk.Button(text='Посчитать', style='my.TButton', width=10, command=self.compute)
		self.draw_button.place(x=125, y=425)

		self.draw_button = ttk.Button(text='Очистить', style='my.TButton', width=10, command=self.clear_canvas)
		self.draw_button.place(x=125, y=525)
		# ===================


	# Основная функция для нахождения искомой окружности
	def compute(self):
		circle = self.find_most_intersecting_circle(list(self.circles))
		if circle is not None:
			x0, y0, r = circle
			self.canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, outline='red')

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

			r = float(self.radius_entry.get())
			if r < 0 or r > 550:
				raise ValueError
			# ========================

			# Проверка, что ввод на канвасе еще активен
			if self.center is not None:
				showinfo('Ошибка', 'Сначала закончите ввод на канвасе!')
				return

			# Рисуем окружность
			self.center = (x, y)
			self.radius = r
			self.draw_circle()
			self.reset()

		except:
			showinfo('Ошибка', 'Данные введены неверно!')
			return

	# Обработка нажатия на канвас
	def on_click(self, event):
		# Если центр еще не сохранен, запоминаем его
		if self.center is None:
			self.center = (event.x, event.y)
		elif self.radius is None:
			# Если центр уже записан, а радиус еще нет, то строим окружность по получившимся точкам
			self.radius = ((event.x - self.center[0]) ** 2 + (event.y - self.center[1]) ** 2) ** 0.5
			self.draw_circle()
			self.reset()

	# Обработка движения курсора по канвасу
	def on_move(self, event):
		# Если был выбран центр, то динамически рисуем окружность для текущего положения курсора
		if self.center is not None:
			if self.temp_circle is not None:
				self.canvas.delete(self.temp_circle)
			self.radius = ((event.x - self.center[0]) ** 2 + (event.y - self.center[1]) ** 2) ** 0.5
			self.temp_circle = self.draw_circle(False, False)
			self.radius = None

	# Функция для рисования окружности
	def draw_circle(self, save=True, show_warning=True):
		x0, y0 = self.center
		r = self.radius
		# Проверка, что окружность влезает на канвас
		if x0 - r < 0 or y0 - r < 0 or x0 + r > self.WIDTH or y0 + r > self.HEIGHT:
			if show_warning: showinfo('Ошибка', 'Окружность не помещается в рабочую область')
			return

		# Рисуем окружность
		circle = self.canvas.create_oval(x0 - r, y0 - r, x0 + r, y0 + r, outline='blue')
		
		# При необходимости добавляем окружность в список окружностей
		if save: self.circles.add((x0, y0, r))
		return circle

	# Сброс данных о текущей окружности
	def reset(self):
		self.center = None
		self.radius = None

	# Алгоритм нахождения искомой окружности
	# Окружности пересекаются, если расстояние между их центрами не больше суммы их радиусов
	def find_most_intersecting_circle(self, circles):
		n = len(circles)
		max_intersections = 0
		max_index = -1

		for i in range(n):
			intersections = 0
			for j in range(n):
				if i == j: continue
				dx = circles[i][0] - circles[j][0]
				dy = circles[i][1] - circles[j][1]
				distance = (dx ** 2 + dy ** 2) ** 0.5 
				if distance <= circles[i][2] + circles[j][2]:
					intersections += 1

			if intersections > max_intersections:
				max_intersections = intersections
				max_index = i

		# Окрашиваем все окружности, пересекающиеся с искомой в зеленый, непересекающиеся - в синий
		if max_index != -1:
			for i in range(n):
				dx = circles[i][0] - circles[max_index][0]
				dy = circles[i][1] - circles[max_index][1]
				distance = (dx ** 2 + dy ** 2) ** 0.5 
				if distance <= circles[i][2] + circles[max_index][2]:
					self.canvas.create_oval(circles[i][0] - circles[i][2],
					circles[i][1] - circles[i][2], circles[i][0] + circles[i][2],
					circles[i][1] + circles[i][2], outline='green')
				else:
					self.canvas.create_oval(circles[i][0] - circles[i][2],
					circles[i][1] - circles[i][2], circles[i][0] + circles[i][2],
					circles[i][1] + circles[i][2], outline='blue')

		return circles[max_index] if max_index != -1 else None
	
	# Очистка канваса
	def clear_canvas(self):
		self.canvas.delete('all')
		self.circles = set()


root = Tk()
app = CircleDrawer(root)
root.mainloop()

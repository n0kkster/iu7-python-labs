# Диваев Александр ИУ7-12Б
# Лаба 13, база данных в текстовом файле

import sys
import os

db_filepath = ['']
initialised = [False]


operands = {'+': 1, '-': 1, '*': 2, '/': 2}

def convert(data):
	out, stack = [], []
	for i in range(len(data)):
		if data[i].isdigit():
			out.append(data[i])

		elif data[i] == "(":
			stack.append(data[i])

		elif data[i] == ")":
			for j in range(len(stack) - 1, -1, -1):
				if stack[j] == "(":
					stack.pop()
					break
				else:
					out.append(stack.pop())

		elif data[i] in operands:
			while stack != []:
				if stack[-1] != "(" and operands[data[i]] <= operands[stack[-1]]:
					out.append(stack.pop())
				else:
					break
			stack.append(data[i])
		else:
			return None
	return out + stack[::-1]


def calculate(rpn):
	while len(rpn) != 1:
		for i in range(2, len(rpn)):
			if rpn[i] in operands:
				rpn[i] = eval(str(rpn[i - 2]) + str(rpn[i]) + str(rpn[i - 1]))
				rpn = rpn[:i - 2] + rpn[i:]
				break
	return int(rpn[0])


# Выходим из программы
def finish():
	sys.exit(0)


# Проверяем, что файл является нашей БД
def check_db_structure():
	with open(db_filepath[0], 'r') as f:
		flag = False
		for line in f:
			flag = True
			items = line.split(';')
			if not (items[1].isdigit() and items[2].isdigit() \
				and items[3] == '\n' and len(items) == 4):
				return False

		return flag


# Выбираем файл для БД
def choose_file():
	clear_screen()
	print_menu()
	print('\rВведите путь к файлу БД: ', end='')

	while True:
		try:
			path = input().strip()
			with open(path, 'a+') as f:
				break

		except OSError:
			clear_screen()
			print_menu()
			print('\rВведите корректный путь к файлу БД: ', end='')	
	
	db_filepath[0] = path
	initialised[0] = check_db_structure()


# Создаем таблицу
def create_table(filepath):
	with open(filepath, 'w') as f:
		clear_screen()
		print_menu()
		print('\rВведите количество записей: ', end='')
		n = input()
		if not n.isdigit():
			return

		n = int(n)

		if n < 0:
			return

		for i in range(n):
			clear_screen()
			print_menu()
			print(f'\rВведите название {i + 1} товара: ', end='')
			name = input().strip()
			
			clear_screen()
			print_menu()
			print(f'\rВведите количество {i + 1} товара: ', end='')
			amount = input().strip()

			clear_screen()
			print_menu()
			print(f'\rВведите цену {i + 1} товара: ', end='')
			price = input().strip()

			price = convert(price.split())

			# Если введенные данные некорректы, останавливаемся
			if not amount.isdigit() or price == None or len(name) == 0:
				print('\x1b[1A')
				print(' ' * 140, end='')
				print('\x1b[1A')
				print('\rДанные были введены некорректно!',
					'Нажмите любую клавишу для продолжения...')
				input()

				f.close()

				# И очищаем записанные раннее данные 
				open(db_filepath[0], 'w').close()

				return
			price = calculate(price)
			f.write(';'.join([name, amount, price, '\n']))

		# Ставим флаг, что текущий файл является БД
		initialised[0] = True


# Запрашиваем подтверждения при инициализации БД, если требуется
def init_db():
	if os.path.exists(db_filepath[0]) and os.path.getsize(db_filepath[0]) != 0:
		clear_screen()
		print_menu()
		print('\rФайл не пуст! Вы уверены, что хотите создать в нем БД [y/n]: ', end='')
		answer = input().split()[0].strip().lower()
		if answer in ['y', 'yes']:
			create_table(db_filepath[0])
	else:
		create_table(db_filepath[0])


# Выводим БД в консоль
def print_db():
	try:
		for _ in range(4):
			print(' ' * 140)
		print('\x1b[4A')

		# Если файл не содержит БД, не выводим
		if not initialised[0]:
			print('Выбранный файл пуст или содержит некорректную структуру!', 
				'Нажмите любую клавишу для продолжения...')
			input()
			return

		with open(db_filepath[0], 'r') as f:
			print('-' * 124)
			print('|{:^40}|{:^40}|{:^40}|'.format('Наименование товара', \
				'Количество товара', 'Цена товара'))
			print('-' * 124)

			for line in f:
				print('|{:^40}|{:^40}|{:^40}|'.format(*(line.split(';'))))
				print('-' * 124)
			input()

	except OSError:

		# Если какой-то нехороший человек удалил файл БД
		# прямо во время работы программы
		print('Файл базы данных не существует или удален!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()


# Добавление строки в конец БД
def insert_into_db():
	try:
		for _ in range(4):
			print(' ' * 140)
		print('\x1b[4A')

		with open(db_filepath[0], 'a') as f:
			if not initialised[0]:
				print('Выбранный файл пуст или содержит некорректную структуру!', 
					'Нажмите любую клавишу для продолжения...')
				input()
				return

			clear_screen()
			print_menu()
			print(f'\rВведите название товара: ', end='')
			name = input().strip()
			
			clear_screen()
			print_menu()
			print(f'\rВведите количество товара: ', end='')
			amount = input().strip()

			clear_screen()
			print_menu()
			print(f'\rВведите цену товара: ', end='')
			price = input().strip()

			price = convert(price.split())

			# Проверяем введенные данные на корректность
			if not amount.isdigit() or price == None or len(name) == 0:
				print('\x1b[1A')
				print(' ' * 140, end='')
				print('\rДанные были введены некорректно!',
					'Нажмите любую клавишу для продолжения...')
				input()

				return

			price = calculate(price)

			f.write(';'.join([name, amount, str(price), '\n']))

	except OSError:
		print('Файл базы данных не существует или удален!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()


# Выводим ошибку
def display_error(msg):
	print('\x1b[5A')
	for _ in range(5):
		print(' ' * 140)
	print('\x1b[5A')

	print(msg, 'Нажмите любую клавишу для продолжения...')
	input()


# Получаем номер поля и значение, по которому будет осуществляться поиск
def get_field_and_value(info=''):

	print(f'Выберите {info}поле, по которому будет осуществлен поиск:',
		'\n1. Наименование товара\n2. Количество товара\n3. Цена за единицу товара')
	column = input()

	if not column.isdigit():
		display_error('Вы ввели некорретные данные!')
		return None, None

	column = int(column)

	if not (0 < column < 4):
		display_error('Вы ввели некорретные данные!')
		return None, None

	print('\x1b[6A')
	for _ in range(6):
		print(' ' * 140)
	print('\x1b[6A')
	
	print('Введите значение выбранного поля, по которому',
		'должен быть осуществлен поиск:')

	value = input()

	if column > 1:
		value = conert(value.split())
		if value == None:
			display_error('Вы ввели некорретные данные!')
			return None, None
		value = calculate(value)


	print('\x1b[3A')
	for _ in range(3):
		print(' ' * 140)
	print('\x1b[3A')

	return column, value


# Ищем строки по одному полю
def find_by_one():
	try:
		for _ in range(4):
			print(' ' * 140)
		print('\x1b[4A')

		with open(db_filepath[0], 'r') as f:
			if not initialised[0]:
				print('Выбранный файл пуст или содержит некорректную структуру!', 
					'Нажмите любую клавишу для продолжения...')
				input()
				return

			column, value = get_field_and_value()

			if column == None or value == None:
				return

			print('-' * 124)
			print('|{:^40}|{:^40}|{:^40}|'.format('Наименование товара', \
				'Количество товара', 'Цена товара'))
			print('-' * 124)

			for line in f:
				if line.split(';')[column - 1] != value:
					continue 

				print('|{:^40}|{:^40}|{:^40}|'.format(*(line.split(';'))))
				print('-' * 124)
			input()

	except OSError:
		print('Файл базы данных не существует или удален!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()


# Ищем строки по двум полям
def find_by_two():
	try:
		for _ in range(4):
			print(' ' * 140)
		print('\x1b[4A')

		with open(db_filepath[0], 'r') as f:
			if not initialised[0]:
				print('Выбранный файл пуст или содержит некорректную структуру!', 
					'Нажмите любую клавишу для продолжения...')
				input()
				return

			column1, value1 = get_field_and_value('первое ')
			if column1 == None or value1 == None:
				return

			column2, value2 = get_field_and_value('второе ')
			if column2 == None or value2 == None:
				return


			print('-' * 124)
			print('|{:^40}|{:^40}|{:^40}|'.format('Наименование товара', \
				'Количество товара', 'Цена товара'))
			print('-' * 124)

			for line in f:
				if line.split(';')[column1 - 1] != value1 \
				or line.split(';')[column2 - 1] != value2: 
					continue 

				print('|{:^40}|{:^40}|{:^40}|'.format(*(line.split(';'))))
				print('-' * 124)
			input()
			
	except OSError:
		print('Файл базы данных не существует или удален!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()


# Обрабатываем запрос пользователя
def process_task(id):
	tasks = [
		finish,
		choose_file,
		init_db,
		print_db,
		insert_into_db,
		find_by_one,
		find_by_two,
	]

	tasks[id]()


# Чистим экран
def clear_screen():

	# Переводим курсор на в позицию (0, 0)
	print('\x1b[H')

	# Заполняем все использованное пространство пустыми символами
	for _ in range(30):
		print(' ' * 140, end='')

	# Возвращаем курсор в (0, 0)
	print('\x1b[H')


# Проверяем ввод пункта меню
def validate_integer(s):
	if s.isdigit():
		if 0 <= int(s) < 7:
			return True
	return False


# Выводим меню
def print_menu():
	print('Выберите действие: ')
	print('1. Выбрать файл для работы')
	print('2. Инициализировать БД')
	print('3. Вывести содержимое БД')
	print('4. Добавить запись в конец БД')
	print('5. Поиск по одному полю')
	print('6. Поиск по двум полям')
	print('0. Выйти из программы')
	print(' ' * 200, end='')


# Обрабатываем выбор пользователя
def get_choice():

	# Выводим меню и приглашение к вводу
	print_menu()
	print('\rВведите номер действия: ', end='')
	choice = input().strip()

	# Пока не получим корректный ввод, будем просить снова
	while not validate_integer(choice):
		clear_screen()
		print_menu()
		print('\rВведите корректный номер действия: ', end='')

		choice = input()

	return int(choice)


# Основная функция
def main():
	print('\x1b[?25l')
	while True:
		clear_screen()
		choice = get_choice()
		process_task(choice)


if __name__ == '__main__':
	main()

# Диваев Александр ИУ7-12Б
# Лаба 14, база данных в бинарном файле

import sys
import os
from struct import pack, unpack, calcsize, error

db_filepath = ['']
initialised = [False]

# Форматная строка для struct
fmt = '<45sqq'

# Размер одной записи
size = calcsize(fmt)

# Выходим из программы
def finish():
	sys.exit(0)


# Проверяем, что файл является нашей БД
def check_db_structure():
	try:
		with open(db_filepath[0], 'rb') as f:
			flag = False
			while b := f.read(size):
				flag = True
				data = unpack(fmt, b)
				name = data[0].decode('utf-8').rstrip('\x00')

				if len(data) == 0 or len(name) == 0:
					return False

			return flag

	except (OSError, error):
		return False


# Выбираем файл для БД
def choose_file():
	clear_screen()
	print_menu()
	print('\rВведите путь к файлу БД: ', end='')

	while True:
		try:
			path = input().strip()
			if os.path.exists(path):
				break
			with open(path, 'wb') as f:
				break

		except OSError:
			clear_screen()
			print_menu()
			print('\rВведите корректный путь к файлу БД: ', end='')	
	
	db_filepath[0] = path
	initialised[0] = check_db_structure()


# Создаем таблицу
def create_table(filepath):
	try:
		with open(filepath, 'wb') as f:
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

				# Если введенные данные некорректы, останавливаемся
				if not (amount.isdigit() and price.isdigit()):
					print('\x1b[1A')
					print(' ' * 140, end='')
					print('\x1b[1A')
					print('\rДанные были введены некорректно!',
						'Нажмите любую клавишу для продолжения...')
					input()

					f.close()

					# И очищаем записанные раннее данные 
					open(db_filepath[0], 'wb').close()

					return

				# Сохраняем запись в БД
				price = int(price)
				amount = int(amount)
				f.write(pack(fmt, bytes(name, 'utf-8'), amount, price))

			# Ставим флаг, что текущий файл является БД
			initialised[0] = True

	except (OSError, error):
		print('Файл базы данных не существует, удален или имеет неверную структуру!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()


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
		clear_half()

		# Если файл не содержит БД, не выводим
		if not initialised[0]:
			print('Выбранный файл пуст или содержит некорректную структуру!', 
				'Нажмите любую клавишу для продолжения...')
			input()
			return

		with open(db_filepath[0], 'rb') as f:
			print('-' * 124)
			print('|{:^40}|{:^40}|{:^40}|'.format('Наименование товара', \
				'Количество товара', 'Цена товара'))
			print('-' * 124)

			# Читам БД по одной записи и выводим
			while b := f.read(size):
				unpacked = unpack(fmt, b)
				s = unpacked[0].decode('utf-8').rstrip('\x00')
				print('|{:^40}|{:^40}|{:^40}|'.format(s, *(unpacked[1:])))
				print('-' * 124)
			input()

	except (OSError, error):
		# Если какой-то нехороший человек удалил файл БД
		# прямо во время работы программы
		print('Файл базы данных не существует, удален или имеет неверную структуру!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()


# Добавление записи в БД
def insert_into_db():
	try:
		clear_half()
		with open(db_filepath[0], 'rb+') as f:
			if not initialised[0]:
				print('Выбранный файл пуст или содержит некорректную структуру!', 
					'Нажмите любую клавишу для продолжения...')
				input()
				return

			# Просим необходимые данные
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

			clear_screen()
			print_menu()
			print(f'\rВведите номер новой записи: ', end='')
			pos = input().strip()

			flag = True
			for c in price:
				if c not in '0123456789+-*/.e ':
					flag = False
					break

			# Проверяем введенные данные на корректность
			if not (amount.isdigit() and flag and len(name) and pos.isdigit()):
				print('\x1b[1A')
				print(' ' * 140, end='')
				print('\rДанные были введены некорректно!',
					'Нажмите любую клавишу для продолжения...')
				input()

				return

			amount = int(amount)
			price = eval(price)
			pos = int(pos) - 1

			# Считаем кол-во записей
			f.seek(0, 2)
			cnt = f.tell() // size
			f.seek(0)

			if not (-1 < pos < cnt + 1):
				print('\x1b[1A')
				print(' ' * 140, end='')
				print('\rДанные были введены некорректно!',
					'Нажмите любую клавишу для продолжения...')
				input()

				return

			# Читаем данные, идущие после вставляемой записи
			f.seek(size * pos)
			next_data = f.read()

			# Пакуем текущую запись
			curr_entry = pack(fmt, bytes(name, 'utf-8'), amount, price)

			# Записываем текущую запись и следующией за ней
			f.seek(size * pos)
			f.write(curr_entry)
			f.write(next_data)

	except (OSError, error):
		# Если какой-то нехороший человек удалил файл БД
		# прямо во время работы программы
		print('Файл базы данных не существует, удален или имеет неверную структуру!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()
	
	except SyntaxError:
		print('Данные были введены некорректно!', 
			'Нажмите любую клавишу для продолжения...')
		input()


# Удаляем запись из БД
def remove_from_db():
	try:
		clear_half()
		with open(db_filepath[0], 'rb+') as f:
			if not initialised[0]:
				print('Выбранный файл пуст или содержит некорректную структуру!', 
					'Нажмите любую клавишу для продолжения...')
				input()
				return

			# Просим данные
			clear_screen()
			print_menu()
			print(f'\rВведите номер удаляемой записи: ', end='')
			pos = input().strip()

			# Проверяем введенные данные на корректность
			if not pos.isdigit():
				print('\x1b[1A')
				print(' ' * 140, end='')
				print('\rДанные были введены некорректно!',
					'Нажмите любую клавишу для продолжения...')
				input()

				return

			pos = int(pos) - 1

			# Считаем кол-во записей
			f.seek(0, 2)
			cnt = f.tell() // size
			f.seek(0)

			if not (-1 < pos < cnt):
				print('\x1b[1A')
				print(' ' * 140, end='')
				print('\rДанные были введены некорректно!',
					'Нажмите любую клавишу для продолжения...')
				input()

				return

			# Запоминаем записи после той, которую надо удалить
			f.seek(size * (pos + 1))
			next_data = f.read()

			# Перезаписываем текущую запись и обрезаем ненужные данные в конце
			f.seek(size * pos)
			f.write(next_data)
			f.truncate(size * (cnt - 1))

			initialised[0] = check_db_structure()

	except (OSError, error):
		# Если какой-то нехороший человек удалил файл БД
		# прямо во время работы программы
		print('Файл базы данных не существует, удален или имеет неверную структуру!', 
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

	if len(value.split()) == 0:
		display_error('Вы ввели некорретные данные!')
		return None, None

	if column > 1:
		# if not value.isdigit():
		# 	display_error('Вы ввели некорретные данные!')
		# 	return None, None

		# value = int(value)

		flag = True
		for c in value:
			if c not in '0123456789+-*/.e ':
				flag = False
				print(f'breaked on {c}')
				input()
				break
		if flag:
			value = eval(value)
		else:
			display_error('Вы ввели некорретные данные!')
			return None, None


	print('\x1b[3A')
	for _ in range(3):
		print(' ' * 140)
	print('\x1b[3A')

	return column, value


# Ищем строки по одному полю
def find_by_one():
	try:
		clear_half()
		with open(db_filepath[0], 'rb') as f:
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

			# Читаем по одной записи и смотрим, подходит ли она нам
			while b := f.read(size):
				data = list(unpack(fmt, b))
				data[0] = data[0].decode('utf-8').rstrip('\x00')
				if data[column - 1] != value:
					continue 

				print('|{:^40}|{:^40}|{:^40}|'.format(*data))
				print('-' * 124)
			input()

	except (OSError, error):
		# Если какой-то нехороший человек удалил файл БД
		# прямо во время работы программы
		print('Файл базы данных не существует, удален или имеет неверную структуру!', 
			'Нажмите любую клавишу для продолжения...')
		initialised[0] = False
		input()


# Ищем строки по двум полям
def find_by_two():
	try:
		clear_half()
		with open(db_filepath[0], 'rb') as f:
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


			# Читаем по одной записи и смотрим, подходит ли она нам
			while b := f.read(size):
				data = list(unpack(fmt, b))
				data[0] = data[0].decode('utf-8').rstrip('\x00')
				if data[column1 - 1] != value1 \
				or data[column2 - 1] != value2: 
					continue 

				print('|{:^40}|{:^40}|{:^40}|'.format(*data))
				print('-' * 124)
			input()
			
	except (OSError, error):
		# Если какой-то нехороший человек удалил файл БД
		# прямо во время работы программы
		print('Файл базы данных не существует, удален или имеет неверную структуру!', 
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
		remove_from_db,
		find_by_one,
		find_by_two,
	]

	tasks[id]()


# Чистим экран
def clear_screen():

	# Переводим курсор на в позицию (0, 0)
	print('\x1b[H')

	# Заполняем все использованное пространство пустыми символами
	for _ in range(70):
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
	print('4. Добавить запись в БД')
	print('5. Удалить запись из БД')
	print('6. Поиск по одному полю')
	print('7. Поиск по двум полям')
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


def clear_half():
	for _ in range(10):
		print(' ' * 140)
	print('\x1b[10A')


# Основная функция
def main():
	print('\x1b[?25l')
	while True:
		clear_screen()
		choice = get_choice()
		process_task(choice)


if __name__ == '__main__':
	main()

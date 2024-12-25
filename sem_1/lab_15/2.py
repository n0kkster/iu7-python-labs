# Диваев Александр, ИУ7-12Б
# Лаба 15. После каждого удвоенного числа вставить его отрицательное значение.


import sys
import os
from struct import pack, unpack, calcsize, error

fmt = '<q'
size = calcsize(fmt)
filepath = ['']

# Выбираем файл для работы
def choose_file():
	print('\rВведите путь к файлу: ', end='')

	while True:
		try:
			path = input().strip()
			if os.path.exists(path):
				break
			with open(path, 'wb') as f:
				break

		except OSError:
			print('\rВведите корректный путь к файлу: ', end='')	
	
	filepath[0] = path


# Запись в файл
def input_numbers():
	try:
		with open(filepath[0], 'wb') as f:
			print('\rВведите числа через пробел: ', end='')

			nums = list(map(int, input().split()))
			for num in nums:
				f.write(pack(fmt, num))

	except ValueError:
		print('\rДанные были введены некорректно!',
				'Нажмите любую клавишу для продолжения...')
		input()
		finish()

	except (OSError, error):
		print('Файл не существует, удален или имеет неверную структуру!', 
			'Нажмите любую клавишу для продолжения...')
		input()
		finish()


# Вставляем удвоенные отрицательные числа
def insert():
	try:
		with open(filepath[0], 'rb+') as f:
			i = 0

			# Читаем по одному числу
			while b := f.read(size):
				curr = unpack(fmt, b)[0]

				# Если текущее отрицательно, то двигаем все после него
				# на одну позицию вперед и вставляем удвоенное текущее
				if curr < 0:
					next_data = f.read()
					f.seek((i + 1) * size)
					f.write(pack(fmt, curr * 2))
					f.write(next_data)
					f.seek((i + 2) * size)
					i += 1
				i += 1
	except (OSError, error):
		print('Файл не существует, удален или имеет неверную структуру!', 
			'Нажмите любую клавишу для продолжения...')
		input()
		finish()


# Вывод чисел на экран
def print_numbers():
	try:
		with open(filepath[0], 'rb') as f:
			print('Получившийся файл: ', end='')
			while b := f.read(size):
				num = unpack(fmt, b)[0]
				print(num, end=' ')


	except (OSError, error):
		print('Файл не существует, удален или имеет неверную структуру!', 
			'Нажмите любую клавишу для продолжения...')
		input()
		finish()


def finish():
	sys.exit(0)

# Основная функция
def main():
	choose_file()
	input_numbers()
	insert()
	print_numbers()


if __name__ == '__main__':
	main()

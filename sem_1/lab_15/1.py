# Диваев Александр, ИУ7-12Б
# Лаба 15. Удалить все положительные числа из файла.


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


# Удаляем положительные
def remove_positive():
	try:
		with open(filepath[0], 'rb+') as f:

			# Считаем кол-во чисел
			f.seek(0, 2)
			cnt = f.tell() // size
			f.seek(0)

			i = 0
			k = 0

			# Читаем файл по одному числу
			while i < cnt:
				curr = unpack(fmt, f.read(size))[0]
				if curr > 0:
					k += 1
				else:
					# Если текущее число неположительно,
					# то алгоритмически свигаем его на количество 
					# найденных положительных чисел 
					f.seek((i - k) * size, 0)
					f.write(pack(fmt, curr))
					f.seek((i + 1) * size, 0)
				i += 1

			# Обрезаем файл
			f.truncate((i - k) * size)

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
	remove_positive()
	print_numbers()


if __name__ == '__main__':
	main()

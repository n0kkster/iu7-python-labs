# Диваев Александр, ИУ7-12Б
# Лаба 15. Сортировка файла методом вставок с барьером.


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


# Сортировка методом вставки с барьером
def sort_file():
	try:
		with open(filepath[0], 'rb+') as f:
			f.seek(0, 2)
			cnt = f.tell() // size
			f.seek(0)

			data = f.read()
			f.seek(0)
			f.write(pack(fmt, 0))
			f.write(data)
			f.seek(0)
			prev = unpack(fmt, f.read(size))[0]
			i = 1

			# Жесть начинается
			while b := f.read(size):
				curr = unpack(fmt, b)[0]
				if prev > curr:
					f.seek(0)
					f.write(pack(fmt, curr))
					j = i - 1
					f.seek(size * j)
					while (fj := unpack(fmt, f.read(size))[0]) > curr:
						f.write(pack(fmt, fj))
						j -= 1
						f.seek(-3 * size, 1)
					f.seek((j + 1) * size)
					f.write(pack(fmt, curr))
				f.seek(size * i)
				prev = unpack(fmt, f.read(size))[0]
				i += 1

			f.seek(size, 0)
			data = f.read()
			f.seek(0, 0)
			f.write(data)
			f.truncate(cnt * size)
			# Жесть заканчивается

	except (OSError, error) as e:
		print('\rФайл не существует, удален или имеет неверную структуру!', 
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
	sort_file()
	print_numbers()


if __name__ == '__main__':
	main()

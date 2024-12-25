# Диваев Александр ИУ7-12Б 
# Найти строку, имеющую наименьшее количество четных элементов

# Просим данные у пользователя
rows_cnt = input('Введите кол-во строк: ').strip()
row_len = input('Введите длину строки: ').strip()

if not (rows_cnt.isdigit() and row_len.isdigit()):
	print('Размеры матрицы могут быть только числовыми!')
else:
	rows_cnt = int(rows_cnt)
	row_len = int(row_len)

	matrix = []
	for i in range(rows_cnt):
		matrix.append([int(x) for x in \
			input(f'Введите {i + 1} строку через пробелы: ').split() if x.isdigit()])
		
		# Если ввод некорректен, останавливаем программу
	if len(matrix[i]) != row_len:
		print('Неправильный ввод')
		break
		
	else:
		# Заводим необходимые для работы программы переменные
		min_even_cnt = len(matrix[0])
		bestrow = None

		for row in matrix:

			# Считаем количество четных в строке
			even_cnt = len([x for x in row if x % 2 == 0])

			# Если меньше минимального, то запоминаем строку
			if even_cnt < min_even_cnt:
				min_even_cnt = even_cnt
				bestrow = row

		# Выводим
		print('Строка, имеющая наименьшее количество четных элементов:')
		for el in bestrow:
			print('{:<5g}'.format(el), end='')

# Диваев Александр ИУ7-12Б 
# Переставить местами строки с наибольшим и наименьшим количеством отрицательных элементов

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
		min_neg_cnt = len(matrix[0])
		max_neg_cnt = 0
		min_neg_ind = 0
		max_neg_ind = 0

		for i in range(rows_cnt):

			# Считаем количество нечетных в строке
			neg_cnt = len([x for x in matrix[i] if x < 0])

			# Если меньше минимального...
			if neg_cnt < min_neg_cnt:
				min_neg_cnt = neg_cnt
				min_neg_ind = i

			# ...или больше максимального, запоминаем индексы
			if neg_cnt > max_neg_cnt:
				max_neg_cnt = neg_cnt
				max_neg_ind = i

		# Меняем
		matrix[min_neg_ind], matrix[max_neg_ind] = matrix[max_neg_ind], matrix[min_neg_ind]

		# Выводим
		print('Получившаяся матрица:')
		for row in matrix:
			for el in row:
				print('{:^5g}'.format(el), end='')
			print()

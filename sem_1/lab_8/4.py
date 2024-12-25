# Диваев Александр ИУ7-12Б 
# Переставить местами столбцы с максимальной и минимальной суммой элементов


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
		max_sum_row_ind = 0
		min_sum_row_ind = 0
		max_sum = sum([matrix[i][0] for i in range(rows_cnt)])
		min_sum = max_sum

		# Идем по столбцам
		for j in range(row_len):

			# Считаем сумму элементов в столбце
			curr_sum = sum([matrix[i][j] for i in range(rows_cnt)])
			
			# Если она больше максимального...
			if curr_sum > max_sum:
				max_sum = curr_sum
				max_sum_row_ind = j

			# ...или меньше минимального, то запоминаем индексы
			if curr_sum < min_sum:
				min_sum = curr_sum
				min_sum_row_ind = j
		
		# Меняем
		for i in range(rows_cnt):
			matrix[i][max_sum_row_ind], matrix[i][min_sum_row_ind] \
			= matrix[i][min_sum_row_ind], matrix[i][max_sum_row_ind]

		# Выводим
		print('Получившаяся матрица:')
		for row in matrix:
			for el in row:
				print('{:^5g}'.format(el), end='')
			print()

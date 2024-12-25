# Диваев Александр ИУ7-12Б 
# Выполнить транспонирование квадратной матрицы

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
		# Транспонируем матрицу
		for i in range(rows_cnt):
			for j in range(i):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		
		# Выводим
		print('Получившаяся матрица:')
		for row in matrix:
			for el in row:
				print('{:^5g}'.format(el), end='')
			print()

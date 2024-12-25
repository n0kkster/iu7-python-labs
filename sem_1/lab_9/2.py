# Диваев Александр ИУ7-12Б 
# 9 ЛАБА
# Программа для поворота квадратной матрицы на 90 градусов
# по часовой стрелке и против часовой стрелки

# Вводим
rows_cnt = int(input('Введите количество строк матрицы: ').strip())
row_len = int(input('Введите количество столбцов матрицы: ').strip())

if rows_cnt != row_len:
	print('Матрица должна быть квадратной!') 

else:

	# Заполненяем матрицу
	matrix = []
	for i in range(rows_cnt):
		matrix.append([int(x) for x in \
			input(f'Введите {i + 1} строку через пробелы: ').split() if x.isdigit()])
		
		if len(matrix[i]) != row_len:
			print('Неправильный ввод')
			break
	else:

		# Поворачиваем по часовой стрелке
		for i in range(rows_cnt // 2):
			for j in range(i, row_len - i - 1):
				matrix[i][j], matrix[j][row_len - i - 1], \
				matrix[row_len - i - 1][row_len - j - 1], \
				matrix[row_len - j - 1][i] = \
				matrix[row_len - j - 1][i], matrix[i][j], \
				matrix[j][row_len - i - 1], \
				matrix[row_len - i - 1][row_len - j - 1]

		# Выводим
		print('Повернутая матрица:')
		for row in matrix:
			for el in row:
				print('{:^5g}'.format(el), end='')
			print()

		# Поворачиваем обратно
		for i in range(rows_cnt // 2):
			for j in range(i, row_len - i - 1):
				matrix[i][j], matrix[j][row_len - i - 1], \
				matrix[row_len - i - 1][row_len - j - 1], \
				matrix[row_len - j - 1][i] = \
				matrix[j][row_len - i - 1], \
				matrix[row_len - i - 1][row_len - j - 1], \
				matrix[row_len - j - 1][i], matrix[i][j]

		# Выводим
		print('Итоговая матрица:')
		for row in matrix:
			for el in row:
				print('{:^5g}'.format(el), end='')
			print()

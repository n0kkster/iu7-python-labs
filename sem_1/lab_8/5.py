# Диваев Александр ИУ7-12Б 
# Найти максимальное значение в квадратной матрице 
# над главной диагональю и минимальное под побочной диагональю

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

		# Если матрица не квадратная, останавливаем
		if len(matrix[i]) != rows_cnt:
			print('Матрица должна быть квадратной!')
			break


	else:
		# Ищем максимальное значение над главной диагональю
		max_el = matrix[0][1]
		for i in range(rows_cnt):
			for j in range(i + 1, rows_cnt):
				max_el = max(max_el, matrix[i][j])

		# Ищем минимальное значение под побочной диагональю
		min_el = matrix[1][-1]
		for i in range(rows_cnt):
			for j in range(rows_cnt - i, rows_cnt):
				min_el = min(min_el, matrix[i][j])

		# Выводим
		print('Максимальный элемент над главной диагональю:', max_el)
		print('Минимальный элемент под побочной диагональю:', min_el)

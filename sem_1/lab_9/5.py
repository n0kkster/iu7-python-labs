rows_cnt = int(input('Введите количество строк матрицы: ').strip())
row_len = int(input('Введите количество столбцов матрицы: ').strip())


matrix = []
for i in range(rows_cnt):
	matrix.append(input(f'Введите {i + 1} строку через пробелы: ').split())
	
	if len(matrix[i]) != row_len:
		print('Неправильный ввод')
		break

else:
	print('Исходная матрица:')
	for row in matrix:
		for el in row:
			print('{:^5}'.format(el), end='')
		print()

	for i in range(rows_cnt):
		for j in range(row_len):
			if matrix[i][j].lower() in 'eyuioa':
				matrix[i][j] = '.'

	print('Итоговая матрица:')
	for row in matrix:
		for el in row:
			print('{:^5}'.format(el), end='')
		print()
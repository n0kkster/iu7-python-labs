matrix_cnt = int(input('Введите количество матриц: ').strip()) # X
rows_cnt = int(input('Введите количество строк матрицы: ').strip()) # Y
row_len = int(input('Введите количество столбцов матрицы: ').strip()) # Z

hypermatrix = []
for j in range(matrix_cnt):
	matrix = []
	for i in range(rows_cnt):
		matrix.append([int(x) for x in \
			input(f'Введите {i + 1} строку {j + 1} матрицы через пробелы: ').split() if x.isdigit()])
		
		if len(matrix[i]) != row_len:
			print('Неправильный ввод')
			break
	else:
		hypermatrix.append(matrix)
		continue
	break

else:
	slice_ind = int(input('Введите номер среза: '))

	print(f'{slice_ind} срез')
	for matrix in hypermatrix:
		for el in matrix[slice_ind - 1]:
			print('{:^5g}'.format(el), end='')
		print()

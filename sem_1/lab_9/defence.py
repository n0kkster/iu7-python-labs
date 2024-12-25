rows_cnt = int(input('Введите количество строк матрицы: ').strip())
row_len = int(input('Введите количество столбцов матрицы: ').strip())

matrix = []
for i in range(rows_cnt):
	matrix.append([int(x) for x in \
		input(f'Введите {i + 1} строку матрицы через пробелы: ').split() if x.isdigit()])
	
	if len(matrix[i]) != row_len:
		print('Неправильный ввод')
		break
else:
	for j in range(row_len):
		column = [matrix[i][j] for i in range(rows_cnt)]
		print(*column[::(-1) ** (j + 1)], end=' ')

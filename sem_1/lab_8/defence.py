# Диваев Александр ИУ7-12Б 
# Защита 8 лабы

from math import ceil

rows_cnt = int(input('Введите количество строк матрицы: ').strip())
row_len = int(input('Введите количество столбцов матрицы: ').strip())


matrix = []
for i in range(rows_cnt):
	matrix.append([int(x) for x in \
		input(f'Введите {i + 1} строку через пробелы: ').split() if x.isdigit()])
	
	if len(matrix[i]) != row_len:
		print('Неправильный ввод')
		break
else:

	right_triangle = []
	left_triangle = []

	for i in range(rows_cnt // 2):
		right_triangle.append(matrix[i][row_len // 2 : row_len // 2 + \
		 ceil((row_len // 2) / (2 ** i))])

	for i in range(rows_cnt // 2, rows_cnt):
		left_triangle.append(matrix[i][row_len // 2 - 1 - \
		 round((row_len // 2) / (2 ** (rows_cnt - i))) : row_len // 2])

	right_triangle = right_triangle[::-1]
	left_triangle = left_triangle[::-1]

	for i in range(rows_cnt // 2):
		matrix[i][row_len // 2 : row_len // 2 + ceil((row_len // 2) \
		 / (2 ** i))] = left_triangle[i][::-1]

	for i in range(rows_cnt // 2, rows_cnt):
		matrix[i][row_len // 2 - 1 - round((row_len // 2) / (2 ** \
		 (rows_cnt - i))) : row_len // 2] = right_triangle[i - rows_cnt // 2][::-1]

	print('Получившаяся матрица:')
	for row in matrix:
		for el in row:
			print('{:^5g}'.format(el), end='')
		print()

# 6
# 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
# 1 2 3 4 5 6
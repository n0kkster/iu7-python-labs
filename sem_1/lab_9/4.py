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
	l = list(map(int, input('Введите элементы списка L через пробел: ').split()))
	if len(l) > rows_cnt:
		print('Длина списка L не может превышать количества строк матрицы.')
	else:
		if max(l) > rows_cnt - 1 or min(l) < 1 - rows_cnt:
			print('Индексы строк в списке L некорректны!')
		else:
			r = []
			for ind in l:
				r.append(max(matrix[ind]))

			avg = sum(r) / len(r)

			print('Получившаяся матрица:')
			for row in matrix:
				for el in row:
					print('{:^5g}'.format(el), end='')
				print()

			print('Список L: ', *l)
			print('Список R: ', *r)
			print(f'Среднее арифметическое элементов списка R: {avg}')

		
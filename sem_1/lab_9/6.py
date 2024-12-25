rows_cnt = int(input('Введите количество строк матрицы A: ').strip())
row_len = int(input('Введите количество столбцов матрицы A: ').strip())


mA = []
for i in range(rows_cnt):
	mA.append([int(x) for x in \
		input(f'Введите {i + 1} строку матрицы A через пробелы: ').split() if x.isdigit()])
	
	if len(mA[i]) != row_len:
		print('Неправильный ввод')
		break
else:
	rows_cnt = int(input('Введите количество строк матрицы B: ').strip())
	row_len = int(input('Введите количество столбцов матрицы B: ').strip())

	if rows_cnt != len(mA) or row_len != len(mA[i]):
		print('Матрицы должны быть одинаковой размерности!')
	else:
		mB = []
		for i in range(rows_cnt):
			mB.append([int(x) for x in \
				input(f'Введите {i + 1} строку матрицы B через пробелы: ').split() if x.isdigit()])
			
			if len(mB[i]) != row_len:
				print('Неправильный ввод')
				break
		else:
			mC = [[0] * row_len for _ in range(rows_cnt)]
			v = []

			for i in range(rows_cnt):
				for j in range(row_len):
					mC[i][j] = mA[i][j] * mB[i][j]

			for j in range(row_len):
				v.append(sum([mC[i][j] for i in range(rows_cnt)]))

			print('Матрица A:')
			for row in mA:
				for el in row:
					print('{:^5g}'.format(el), end='')
				print()

			print('Матрица B:')
			for row in mB:
				for el in row:
					print('{:^5g}'.format(el), end='')
				print()

			print('Матрица C:')
			for row in mC:
				for el in row:
					print('{:^5g}'.format(el), end='')
				print()

			print('Список V: ', *v)
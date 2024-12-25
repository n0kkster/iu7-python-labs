# Диваев Александр ИУ7-12Б 
# 9 ЛАБА
# Программа для подсчета характеристик
# одной матрицы в зависимости от второй


# Ввод
rows_cnt = int(input('Введите количество строк матрицы D: ').strip())
row_len = int(input('Введите количество столбцов матрицы D: ').strip())

# Заполняем матрицы по очень сложной структуре
mD = []
for i in range(rows_cnt):
	mD.append([int(x) for x in \
		input(f'Введите {i + 1} строку матрицы D через пробелы: ').split() if x.isdigit()])
	
	if len(mD[i]) != row_len:
		print('Неправильный ввод')
		break
else:
	rows_cnt = int(input('Введите количество строк матрицы Z: ').strip())
	row_len = int(input('Введите количество столбцов матрицы Z: ').strip())

	if rows_cnt != len(mD):
		print('Количество строк матрицы D должно быть равно количеству строк '
			'матрицы Z!')
	else:
		mZ = []
		for i in range(rows_cnt):
			mZ.append([int(x) for x in \
				input(f'Введите {i + 1} строку матрицы Z через пробелы: ').split() if x.isdigit()])
			
			if len(mZ[i]) != row_len:
				print('Неправильный ввод')
				break
		else:

			# Считаем необходимые характеристики
			lG = []
			for i in range(len(mD)):
				cnt = len([x for x in mD[i] if x > sum(mZ[i])])
				lG.append(cnt)

			maxcnt = max(lG)

			# Выводим
			print('Матрица Z:')
			for row in mZ:
				for el in row:
					print('{:^5g}'.format(el), end='')
				print()

			print('Матрица D до преобразования:')
			for row in mD:
				for el in row:
					print('{:^5g}'.format(el), end='')
				print()

			for i in range(len(mD)):
				for j in range(len(mD[i])):
					mD[i][j] *= maxcnt

			print('Матрица D после преобразования:')
			for row in mD:
				for el in row:
					print('{:^5g}'.format(el), end='')
				print()

			print('Список G: ', *lG)

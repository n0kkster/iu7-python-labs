# Диваев Александр ИУ7-12Б 
# Найти столбец, имеющий наибольшее количество чисел, являющихся степенями 2

from math import log

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

		# Заводим необходимые для работы программы переменные
		ind = -1
		max_cnt = 0

		# Идем по столбцам
		for j in range(row_len):
			curr_cnt = 0
			for i in range(rows_cnt):

				# Пропускаем нечетные элементы
				if matrix[i][j] < 0: 
					continue

				# Проверяем является ли степенью двойки
				power = log(matrix[i][j], 2)
				if int(power) == power:
					curr_cnt += 1

			# Если количество в столбце больше макимального, обновляем переменные
			if curr_cnt > max_cnt:
				max_cnt = curr_cnt
				ind = j

		# Выводим
		if ind > -1:
			print('Столбец, имеющий наибольшее количество степеней двойки:')
			for row in matrix:
				print('{:^5g}'.format(row[ind]))
		else:
			print('Степеней двойки нет')

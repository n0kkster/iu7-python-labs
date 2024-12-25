# Диваев Александр ИУ7-12Б 
# 9 ЛАБА
# Программа для заполнения матрицы по заданной формуле и подсчета
# некоторых ее параметров

from math import sin

# Просим данные у пользователя
d = list(map(int, input('Введите элементы первого списка через пробел: ').split()))
f = list(map(int, input('Введите элементы второго списка через пробел: ').split()))

# Определяем длины введенных списков
ld = len(d)
lf = len(f)

if ld == 0 or lf == 0:
	print('Матрицы не существует!')

else:
	# Создаем матрицу нужного размера, заполененную нулями
	matrix = [[0] * lf for i in range(ld)]

	# Создаем необходимые списки
	av = []
	l = []

	for j in range(ld):
		pos_cnt = 0
		pos_sum = 0

		# Подсчитываем среднее арифметическое положительных
		for k in range(lf):
			matrix[j][k] = sin(d[j] + f[k])
			if matrix[j][k] > 0:
				pos_cnt += 1
				pos_sum += matrix[j][k]

		# Создаем переменные и инициализируем их дефолтными значениями
		avg = -1
		less_than_avg_cnt = len(matrix[j])

		# При необходимости обновляем
		if pos_cnt != 0:
			avg = pos_sum / pos_cnt
			less_than_avg_cnt = len([x for x in matrix[j] if x < avg])
		

		# Добавляем значения к текущей строке матрицы
		matrix[j].append(avg)
		matrix[j].append(less_than_avg_cnt)

	# Выводим
	print('Получившаяся матрица:')
	for row in matrix:
		for el in row:
			print('{:^8.2g}'.format(el), end='')
		print()

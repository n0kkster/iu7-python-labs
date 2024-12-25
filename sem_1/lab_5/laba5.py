# Диваев Александр, ИУ7-12Б
# Программа для вычисления суммы бесконечного ряда
# с точностью эпсилон.

x = 1
# x = float(input('Введите значение аргумента: '))
e = float(input('Введите необходимую точность: '))
step = int(input('Введите шаг печати: '))
max_iters = int(input('Введите максимальное количество итераций: '))

# Задаем необходимые для работы программы переменные
width = 42
iters = 0
s = 0

# Выводим шапку таблицы
print('-' * width)
print('| № итерации | {:^11} | {:^11} |'.format('t', 's'))
print('-' * width)

# Считаем сумму ряда
for i in range(1, max_iters + 1):
	# Считаем текущий член ряда по формуле
	n = i * x
	t = (n / (2 * n - 1)) ** n

	# Прибавляем его к сумме
	s += t

	# Выводим строки таблицы, учитывая заданный шаг
	if (i - 1) % step == 0:
		print('| {:<11}| {:^11.5g} | {:^11.5g} |'.format(i, t, s))

	# Считаем количество пройденных итераций
	iters += 1

	# Если достигли нужной точности, останавливаемся
	if abs(t) <= e: 
		# Выводим низ таблицы
		print('-' * width)
		print(f'Сумма бесконечного ряда = {s:.5g}, количество итераций: {iters}.')
		break
else:
	# Выводим низ таблицы
	print('-' * width)
	print(f'Не удалось достигнуть указанной точности '
		f'за требуемое количество итераций ({max_iters}).')

from math import pi

def z(a):
	return 4.81 * a ** 3 + 2.44 * a ** 2 - 14.78 * a - 5.99

def q(a):
	return 6.31 * a ** 2 - 8.24 * pi * a - 2

def graph(a):
	return z(a)


start, end, step = map(float, input('Введите начальную и конечную точки и шаг через пробел: ').split())


# Заводим необходимые для работы программы переменные
current = start
remain = abs(end - current)
mn = 10 ** 9
mx = -10 ** 9
qmin = 10 ** 9
zmin = 10 ** 9
width = 150
x_maxlen = 0

# Выводим заголовок таблицы
print('-' * 40)
print('|{:^12}|{:^12}|{:^12}|'.format('x', 'z', 'q'))
print('|' + '-' * 39)

count = int((end - start) / step + 1)

# Выводим содержание таблицы
for i in range(count):

	x_maxlen = max(x_maxlen, len(f'{current}'))
	mn = min(mn, graph(current))
	mx = max(mx, graph(current))

	qmin = min(qmin, q(current))
	zmin = min(zmin, z(current))


	print('|{:^12.5g}|{:^12.5g}|{:^12.5g}|'.format(current, z(current), q(current)))
 
	current += step
	current = round(current, 10)
	remain -= abs(step)
 
# Выводим нижнюю часть таблицы
print('-' * 40)

n = int(input('Введите количество засечек от 4 до 8: '))

# График функции
# Считаем значения, необходимые для построения графика функции
dst = (mx - mn) / (n - 1)
total_offset = 1 + x_maxlen + len(f'{mn:.5g}')
reduced_width = width - len(f'{mx:.5g}') - total_offset
graph_width = width - (1 + x_maxlen)
hasZero = (mx >= 0) and (mn <= 0)
zero_index = int(abs(mn) / abs(mx - mn) * graph_width)

# Выводим ось ординат
print(' ' * (1 + x_maxlen) + f'{mn:.5g}', end='')
for i in range(1, n - 1):
	curr_y = mn + dst * i
	offset = int(reduced_width // (n - 2)) - len(f'{curr_y:.5g}') \
		- reduced_width // (n - 2) // n

	print(' ' * offset + f'{curr_y:.5g}', end='')
	total_offset += int(reduced_width // (n - 2))

offset = width - total_offset - len(f'{mx:.5g}') \
	+ reduced_width // (n - 2) // n * (n - 2)

print(' ' * offset + f'{mx:.5g}')
print('-' * (width + 1))


current = start
remain = abs(end - current)

# Выводим значения по оси абсцисс
for i in range(count):
	curr_y = graph(current)
	
	offset = int((curr_y - mn) / abs(mx - mn) * (graph_width))

	if hasZero:
		if zero_index < offset:
			print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * zero_index + 
				'|' + ' ' * (offset - zero_index - 1) + '*')

		elif zero_index > offset:
			print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * offset +
				f'*' + ' ' * (zero_index - offset - 1) + '|')

		else:
			print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * offset + '*')

	else:
		print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * offset + '*')

	current += step
	current = round(current, 15)
	remain -= abs(step)

# Дополнительное задание
print(f'\nQmin + Zmin = {(qmin + zmin):.5g}')

# График производной
# Считаем значения, необходимые для построения графика производной
dst = (mx - mn) / (n - 1)
total_offset = 1 + x_maxlen + len(f'{mn:.5g}')
reduced_width = width - len(f'{mx:.5g}') - total_offset
graph_width = width - (1 + x_maxlen)
hasZero = (mx >= 0) and (mn <= 0)
zero_index = int(abs(mn) / abs(mx - mn) * graph_width)

# Выводим ось ординат
print(' ' * (1 + x_maxlen) + f'{mn:.5g}', end='')
for i in range(1, n - 1):
	curr_y = mn + dst * i
	offset = int(reduced_width // (n - 2)) - len(f'{curr_y:.5g}') \
		- reduced_width // (n - 2) // n

	print(' ' * offset + f'{curr_y:.5g}', end='')
	total_offset += int(reduced_width // (n - 2))

offset = width - total_offset - len(f'{mx:.5g}') \
	+ reduced_width // (n - 2) // n * (n - 2)

print(' ' * offset + f'{mx:.5g}')
print('-' * (width + 1))


current = start
remain = abs(end - current)

# Выводим значения по оси абсцисс
for i in range(count):
	curr_y = (graph(current) - graph(current - step)) / step 
	
	offset = int((curr_y - mn) / abs(mx - mn) * (graph_width))

	if hasZero:
		if zero_index < offset:
			print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * zero_index + 
				'|' + ' ' * (offset - zero_index - 1) + '*')

		elif zero_index > offset:
			print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * offset +
				f'*' + ' ' * (zero_index - offset - 1) + '|')

		else:
			print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * offset + '*')

	else:
		print(f'{current}' + ' ' * (x_maxlen - len(f'{current}')) + '|'  + ' ' * offset + '*')

	current += step
	current = round(current, 15)
	remain -= abs(step)

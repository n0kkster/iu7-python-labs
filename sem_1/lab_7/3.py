# Диваев Александр ИУ7-12Б
# Поиск элемента с наибольшим количеством подряд
# идущих цифр в списке строк

# Просим у пользователя данные
lst = input('Введите список строк через пробел: ').split()

# Задаем необходимые переменные
maxdigits = 0
bestel = ''

for el in lst:

	# Запоминаем текущий элемент 
	tmp = el

	# Заводим переменную для хранения количества подряд идущих цифр
	digits_cnt = 0

	# Меняем все цифры на 0
	for x in range(10):
		el = el.replace(str(x), '0')

	# Если в строке есть хоть одна цифра
	if '0' in el:

		# Смотрим максимальное количество 0, идущих подряд 
		for k in range(len(el) - 1, -1 , -1):
			if '0' * k in el:
				digits_cnt = k
				break

	# Обновляем переменные при необходимости
	if digits_cnt > maxdigits:
		maxdigits = digits_cnt
		bestel = tmp

# Вывод
print(f'Элемент с наибольшим количеством цифр, идущих подряд: {bestel}')

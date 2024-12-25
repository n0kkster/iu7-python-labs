# Диваев Александр ИУ7-12Б
# Лаба 11
# Сортировка списка методом вставок с барьером

import random
from time import perf_counter_ns

# Проверка вводимых данных на корректность
def check_valid(s):
	if len(s) == 0: return False
	if s[0] in '+-':
		s = s[1:]
	return s.isdigit()

# Сортировка вставками с барьером
def sort(lst):
	shuffles = 0
	start = perf_counter_ns() 

	lst = [0] + lst
	for i in range(1, len(lst)):
		if lst[i - 1] > lst[i]:
			lst[0] = lst[i]
			shuffles += 1
			j = i - 1
			while lst[j] > lst[0]:
				lst[j + 1] = lst[j]
				shuffles += 1
				j -= 1
			lst[j + 1] = lst[0]
			shuffles += 1
		# print(lst)
	end = perf_counter_ns() 

	elapsed = (end - start) / 10**6

	return lst[1:], shuffles, elapsed

# Основная функция
def main():

	# Создаем тестовый список
	test_list = []

	# Вводим элемента тестового списка
	print('Введите элементы тестового списка через пробел: ')
	for x in input().split():

		# Проверяем их на корректность
		if not check_valid(x):
			print('Некорректный ввод!')
			return

		test_list.append(int(x))

	# Если тестовый список пуст, оповещаем об этом пользователя
	if len(test_list) == 0:
		print('Тестовый список пуст!')

	else:

		# Иначе сортируем и выводим
		test_list = sort(test_list)[0]
		print('Отсортированный тестовый список: ', end='')
		print(*test_list)

	# Вводим размерности и проверяем их на корректность
	n1 = input('Введите размерность первого списка: ')
	if not check_valid(n1):
		print('Некорректный ввод!')
		return

	n1 = int(n1)
	if n1 < 0:
		print('Некорректный ввод!')
		return

	
	n2 = input('Введите размерность второго списка: ')
	if not check_valid(n2):
		print('Некорректный ввод!')
		return

	n2 = int(n2)
	if n2 < 0:
		print('Некорректный ввод!')
		return
	

	n3 = input('Введите размерность третьего списка: ')
	if not check_valid(n3):
		print('Некорректный ввод!')
		return

	n3 = int(n3)
	if n3 < 0:
		print('Некорректный ввод!')
		return


	# Для каждой размерности создаем три списка:

	# Упорядоченный
	l1_straight = list(range(0, n1))
	
	# Рандомный
	l1_random = l1_straight.copy()
	random.shuffle(l1_random)
	
	# Обратно упорядоченный
	l1_reversed = l1_straight[::-1]

	l2_straight = list(range(0, n2))
	l2_random = l2_straight.copy()
	random.shuffle(l2_random)
	l2_reversed = l2_straight[::-1]

	l3_straight = list(range(0, n3))
	l3_random = l3_straight.copy()
	random.shuffle(l3_random)
	l3_reversed = l3_straight[::-1]


	# Сортируем все списки, считаем время и количество перестановок
	s1_st, t1_st = sort(l1_straight)[1:]
	s1_rand, t1_rand = sort(l1_random)[1:]
	s1_rev, t1_rev = sort(l1_reversed)[1:]

	s2_st, t2_st = sort(l2_straight)[1:]
	s2_rand, t2_rand = sort(l2_random)[1:]
	s2_rev, t2_rev = sort(l2_reversed)[1:]

	s3_st, t3_st = sort(l3_straight)[1:]
	s3_rand, t3_rand = sort(l3_random)[1:]
	s3_rev, t3_rev = sort(l3_reversed)[1:]
	

	# Выводим таблицу
	print('-' * 135)
	print('|{:^40}|{:^30}|{:^30}|{:^30}|'.format('Размерность', n1, n2, n3))
	print('|' + '-' * 133 + '|')

	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('', '', '', '', '', '', ''))
	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('', 'Время, мс', 'Перестановки', 'Время, мс',\
		 'Перестановки', 'Время, мс', 'Перестановки'))
	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('', '', '', '', '', '', ''))	
	print('|' + '-' * 133 + '|')

	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('', '', '', '', '', '', ''))
	print('|{:^40}|{:^13.6g}|{:^16}|{:^13.6g}|{:^16}|{:^13.6g}|{:^16}|'\
		.format('Упорядоченный список', t1_st, s1_st, t2_st, s2_st, t3_st, s3_st))
	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('', '', '', '', '', '', ''))
	print('|' + '-' * 133 + '|')

	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('', '', '', '', '', '', ''))
	print('|{:^40}|{:^13.6g}|{:^16}|{:^13.6g}|{:^16}|{:^13.6g}|{:^16}|'\
		.format('Случайный список', t1_rand, s1_rand, t2_rand, s2_rand, t3_rand, \
			s3_rand))
	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('', '', '', '', '', '', ''))
	print('|' + '-' * 133 + '|')

	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('Обратно', '', '', '', '', '', ''))
	print('|{:^40}|{:^13.6g}|{:^16}|{:^13.6g}|{:^16}|{:^13.6g}|{:^16}|'\
		.format('упорядоченный', t1_rev, s1_rev, t2_rev, s2_rev, t3_rev, s3_rev))
	print('|{:^40}|{:^13}|{:^16}|{:^13}|{:^16}|{:^13}|{:^16}|'\
		.format('список', '', '', '', '', '', ''))
	print('-' * 135)

# Запускаем основную функцию
main()

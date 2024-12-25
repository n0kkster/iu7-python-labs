# Диваев Александр ИУ7-12Б
# Лаба 11
# Защита (сортировка пузырьком с флагом)

from random import shuffle
from time import perf_counter_ns

def check_valid(s):
	if len(s) == 0: return False
	if s[0] in '+-':
		s = s[1:]
	return s.isdigit()

def sort(lst):
	start = perf_counter_ns() 

	for i in range(len(lst) - 1):
		flag = True
		for j in range(len(lst) - 1 - i):
			if lst[j] > lst[j + 1]:
				lst[j], lst[j + 1] = lst[j + 1], lst[j]
				flag = False
		if flag:
			break

	end = perf_counter_ns() 

	elapsed = (end - start) / 10**6
	return lst, elapsed

def main():

	test_list = list(range(100))
	# shuffle(test_list)

	# print('Введите элементы тестового списка через пробел: ')
	# for x in input().split():

	# 	if not check_valid(x):
	# 		print('Некорректный ввод!')
	# 		return

	# 	test_list.append(int(x))

	print('Отсортированный список: ', end='')
	lst, time = sort(test_list)
	print(*lst)
	print(time)


main()

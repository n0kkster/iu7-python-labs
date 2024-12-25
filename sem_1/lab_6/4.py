# Диваев Александр ИУ7-12Б
# Поиск убывающей последовательности отрицательных чисел, 
# модуль каждого из которых является простым числом


# Просим данные у пользователя
lst = [int(x) for x in input('Введите элементы списка через пробел: ').split()]

# Заводим списки с текущей и маскимальной последовательностью
seq = []
maxseq = []

# Проверяем, удовлетворяет ли первый элемент условию
el = lst[0]
if el < 0 and el != -1:
	prime = True
	for i in range(2, int(abs(el) ** 0.5) + 1):
		if abs(el) % i == 0: 
			prime = False
			break

	if prime:
		seq.append(el)

# Запускаем основной цикл
for i in range(1, len(lst)):
	el = lst[i]

	# Проверяем модуль элемента на простоту
	prime = True
	for x in range(2, int(abs(el) ** 0.5) + 1):
		if abs(el) % x == 0: 
			prime = False
			break

	if prime and el < 0 and el < lst[i - 1] and el != -1:
		seq.append(el)
	else:
		if len(seq) > len(maxseq):
			maxseq = seq.copy()
		seq = []

if len(seq) > len(maxseq):
	maxseq = seq.copy()

print(*maxseq)

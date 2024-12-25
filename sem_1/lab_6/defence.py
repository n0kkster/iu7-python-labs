# Диваев Александр ИУ7-12Б
# Поиск последовательности Фибоначчи максимальной длины


lst = [int(x) for x in input('Введите элементы списка через пробел: ').split()]

seq = []
maxseq = []

for i in range(2, len(lst)):
	if lst[i] == lst[i - 1] + lst[i - 2]:
		if lst[i - 2] not in seq:
			seq.append(lst[i - 2])
		if lst[i - 1] not in seq:
			seq.append(lst[i - 1])

		seq.append(lst[i])
	else:
		if len(seq) > len(maxseq):
			maxseq = seq.copy()
			seq = []

if len(seq) > len(maxseq):
	maxseq = seq.copy()

if len(maxseq) != 0:
	print('Последовательность чисел Фибоначчи максимальной длины:', *maxseq)
else:
	print('Последовательность пустаd')
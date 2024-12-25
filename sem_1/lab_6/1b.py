# Диваев Александр ИУ7-12Б
# Добавление элемента в список алгоритмически

# Просим данные у пользователя
lst = [int(x) for x in input('Введите элементы списка через пробел: ').split()]
el = int(input('Введите дополнительный элемент: '))
ind = int(input('Введите индекс дополнительного элемента: '))

# Добавляем None в конец списка
lst.append(None)

# Сдвигаем элементы после искомого вправо
for i in range(len(lst) - 1, ind, -1):
	lst[i] = lst[i-1]

lst[ind] = el

print('Полученный список:', *lst)

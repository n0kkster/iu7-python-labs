# Диваев Александр ИУ7-12Б
# Добавление элемента в список

# Просим данные у пользователя
lst = [int(x) for x in input('Введите элементы списка через пробел: ').split()]
el = int(input('Введите дополнительный элемент: '))
ind = int(input('Введите индекс дополнительного элемента: '))

# Добавляем элемент в список
lst.insert(ind, el)

print('Полученный список:', *lst)

# Диваев Александр ИУ7-12Б
# Удаление всех положительных элементов

# Считываем только неположительные элементы,
# ибо положительные все-равно удалим позже
lst = [x for x in list(map(int, input('Введите элементы списка через пробел: ').split())) if x <= 0]

# Вывод
print('Полученный список:', *lst)

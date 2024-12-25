from math import log
from math import nan, isnan


# Данная функция
def f(x):
	return -x**2


# Первоообразная функции
def f_antiderivative(x):
	return -1/3 * x**3


# Проверка строки на десятичную дробь
def check_valid(s):
	if 'e' in [s[0], s[-1]]:
		return False
	if s[0] in '-+':
		s = s[1:]
	if 'e-' in s:
		s = s.replace('-', '', 1)
	return s.replace('.', '', 1).replace('e', '', 1).isnumeric()

# Левые прямоугольники
def left_rect(n, start, stop):
	h = (stop - start) / n
	s = 0
	for i in range(n):
		s += f(start + h * i)
	s *= h
	return s


# 3/8
def three_eights(n, start, stop):
	if n % 3 != 0: 
		return nan

	h = (stop - start) / n
	s = 0
	for i in range(0, n - 2, 3):
		s += f(start + i * h) + 3 * f(start + (i + 1) * h) + 3 \
		* f(start + (i + 2) * h) + f(start + (i + 3) * h)
	s /= 8
	s *= h
	return s * 3


# Подбор числа делений для получения интеграла с необходимой точностью
def get_best_integral(method, eps, start, stop):
	n = 3
	while abs(method(n, start, stop) - method(2 * n, start, stop)) > eps:
		n *= 2
	return n, method(n, start, stop)


# Вводим
s_start = input('Введите начало отрезка: ').strip()
s_stop = input('Введите конец отрезка: ').strip()
n1 = input('Введите первое количество делений: ').strip()
n2 = input('Введите второе количество делений: ').strip()

# Проверяем ввод пользователя
if check_valid(s_start) and check_valid(s_stop) \
and n1.isdigit() and n2.isdigit():

	start = float(s_start)
	stop = float(s_stop)
	n = [int(n1), int(n2)]
	if stop > start and n[0] > 0 and n[1] > 0:
		if n[0] % 3 == n[1] % 3 == 0:

			# Считаем интегралы
			integral_first = [left_rect(n[0], start, stop), left_rect(n[1], start, stop)]
			integral_second = [three_eights(n[0], start, stop), three_eights(n[1], start, stop)]

			# Считаем точный интеграл
			real_integral = f_antiderivative(stop) - f_antiderivative(start)
			
			# Считаем погрешности
			abs_diffs = [abs(x - real_integral) for x in (integral_first + integral_second)]
			rel_diffs = [x / real_integral for x in abs_diffs]

		else:

			# Считаем интегралы
			integral_first = [left_rect(n[0], start, stop), left_rect(n[1], start, stop)]
			integral_second = [three_eights(n[0], start, stop), three_eights(n[1], start, stop)]

			# Считаем точный интеграл
			real_integral = f_antiderivative(stop) - f_antiderivative(start)
			
			# Считаем погрешности
			abs_diffs = []
			rel_diffs = []

			for x in (integral_first + integral_second):
				if isnan(x):
					abs_diffs.append(nan)
				else:
					abs_diffs.append(abs(x - real_integral))
			for x in abs_diffs:
				if isnan(x):
					rel_diffs.append(x)
				else:
					rel_diffs.append(x / real_integral)

		
		# Выводим интегралы
		print()
		print('{:^15}N1{:^15}N2'.format('', ''))
		print('Метод ЛП {:^15.7g}{:^15.7g}'.format(*integral_first))
		print('Метод 3/8{:^15.7g}{:^15.7g}'.format(*integral_second).replace('nan', '----'))
		print('Настоящее значение интеграла: {:.7g}'.format(real_integral))
		print()

		# Выводим погрешности
		for i in range(4):
			print('Абсолютная погрешность метода {} при числе делений {:.7g}: {:.7g}'
				  .format(i // 2 + 1, n[i % 2], abs_diffs[i]).replace('nan', '----'))
			print('Относительная: {:.7g}'.format(rel_diffs[i]).replace('nan', '----'))
			print()
		
		# Вводим требуемую точность
		s_e = input('Введите Epsilon: ').strip()
		if check_valid(s_e):
			if float(s_e) > 0:

				# Считаем интеграл худшим методом
				if abs_diffs.index(min(abs_diffs)) >= 2:
					good_n, good_integral = get_best_integral(left_rect, float(s_e), start, stop)
					print('Худший метод - метод левых прямоугольников')

				else:
					good_n, good_integral = get_best_integral(three_eights, float(s_e), start, stop)
					print('Худший метод - метод 3/8')
				
				# Вывод приближенного значения
				print('Приближенное значение интеграла: {:.7g}'.format(good_integral))
				print('Необходимое количество делений: {:.7g}'.format(good_n))
			else:
				print('Некорректный ввод!')
		else:
			print('Некорректный ввод!')
	else:
		print('Некорректный ввод!')
else:
	print('Некорректный ввод!')

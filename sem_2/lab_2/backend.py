from math import *
import numpy as np

from scipy.optimize import brentq
from sympy.parsing.sympy_parser import parse_expr
from sympy import symbols, diff, lambdify


def newthon_method(func, derivative, x, precision, nmax):
	for i in range(nmax):
		if abs(derivative(x)) < 1e-9:
			return -1, x

		if abs(func(x)) < precision:
			return i, x
		x = x - func(x) / derivative(x)

	return -1, x		


def process_data(func_string, precision, start, stop, step, nmax):
	current_start = start
	roots = []

	while round(stop, 6) - round(current_start, 6) > 1e-9:
		current_stop = min(round(current_start + step, 6), stop)

		try:
			func = lambda x: eval(func_string)
			derivative = lambdify(symbols('x'), diff(parse_expr(func_string),
			 symbols('x')), modules='scipy')

			if func(current_stop) == 0:
				roots.append([f'[{current_start};{current_stop}]', 
					current_stop, 0, 0, 0])

			elif func(current_start) * func(current_stop) < 0:
				# root, result = brentq(func, current_start, current_stop,
				# 					  rtol=precision, maxiter=nmax, full_output=True, disp=False)
				# iterations = result.iterations
				# roots.append([f'[{current_start};{current_stop}]', 
				# 	root, f'{func(root):.0e}', iterations, 0 if result.converged else 1])

				iters, root = newthon_method(func, derivative, current_start, precision, nmax)
				if iters < 0 or not (current_start <= root <= current_stop):
					iters, root = newthon_method(func, derivative, current_stop, precision, nmax)
					if iters < 0 or not (current_start <= root <= current_stop):
						roots.append([f'[{current_start};{current_stop}]', 
							root, f'{func(root):.0e}', iters, 1])
					else:
						roots.append([f'[{current_start};{current_stop}]', 
							root, f'{func(root):.0e}', iters, 0])
				else:
					roots.append([f'[{current_start};{current_stop}]', 
							root, f'{func(root):.0e}', iters, 0])


			current_start = current_stop

		except Exception as e:
			raise
			return roots, (False, 'Функция задана неверно!')
	return roots, (True, 'OK')


def gen_plot_data(func_string, start, stop):
	x = np.linspace(start, stop, 2000)
	y = []

	try:
		func = lambda x: eval(func_string)
		y = [func(xval) for xval in x]

	except Exception as e:
		return x, y, (False, 'Функция задана неверно!')

	return x, y, (True, 'OK')


def find_extremums(func_string, start, stop, step):
	return find_derivative_roots(func_string, start, stop, step)


def find_inflection_points(func_string, start, stop, step):
	return find_derivative_roots(func_string, start, stop, step, 2)


def find_derivative_roots(func_string, start, stop, step, n=1):
	current_start = start
	roots = []

	while round(stop, 6) - round(current_start, 6) > 1e-9:
		current_stop = min(round(current_start + step, 6), stop)

		try:
			func = lambda x: eval(func_string)
			x = symbols('x')
			derivative = lambdify(x, diff(parse_expr(func_string), x, n), modules='scipy')

			if derivative(current_start) * derivative(current_stop) <= 0:
				root, result = brentq(derivative, current_start, 
					current_stop, full_output=True, disp=False)
				roots.append((root, func(root)))

			current_start = current_stop

		except Exception as e:
			raise
			return roots, (False, 'Функция задана неверно!')

	return roots, (True, 'OK')


if __name__ == '__main__':
	print('Вам стоит запустить frontend.py')

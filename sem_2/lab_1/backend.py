import re

MODE = 109
PRECISION = 6


def validate(num, mode):
	if mode == 910:
		if '9' in num:
			return False

	res = re.match(r'^[+-]?([0-9]+[.]?[0-9]*|[0-9]*\.[0-9]+)(e[-+]?[0-9]+)?$', num)
	return res != None


# number, old base, new base
def convert(num, n, k):
	try:
		sign = ''
		if num[0] == '-': 
			sign = '-'
			num = num[1:]

		int_part, decimal_part = str(float(num)).split('.')
		converted = convert_int(int_part, n, k) + convert_decimal(decimal_part, n, k)
		return True, sign + converted
	except Exception as e:
		return False, e
	

def convert_decimal(num, n, k):
	s = ''
	if k == 10:
		new_dec = 0
		for i, el in enumerate(num):
			new_dec += round(int(el) * n ** (-i - 1), PRECISION)
		s = str(new_dec)[2:]
	else:
		num = float('0.' + num)
		for i in range(PRECISION):
			num *= k
			s += str(num).split('.')[0]
			num = float('0.' + str(num).split('.')[1])
	return '.' + s[0] + s[1:].rstrip('0')


def convert_int(num, n, k):
	num = int(num, n)
	s = ''
	while num > 0:
		s = str(num % k) + s
		num //= k
	return s if len(s) > 0 else '0'


def process_data(num, mode):
	if not validate(num, mode):
		return False, 'Введено некорректное число!'

	if mode == 109:
		return convert(num, 10, 9)
	elif mode == 910:
		return convert(num, 9, 10)
	else:
		return False, 'error'


if __name__ == '__main__':
	print('Вам стоит запустить frontend.py')

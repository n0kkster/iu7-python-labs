# Диваев Александр ИУ7-12Б
# Лаба 12, текстовый процессор


import sys
from math import floor
from string import punctuation


# Наш текст
text = [
	"Артем поежился, представляя себе туннель за пятисотым метром и то, что туда однажды",
	"придется идти. Это было действительно страшно. За 750 - 250 метр на север не отваживался",
	"ходить никто. Патрули доезжали до трехсотого и, осветив пограничный столб прожектором",
	"со своей дрезины и убедившись, что никакая дрянь не перепозла за него, торопливо",
	"возвращались. Разведчики, здоровые прожженные мужики, бывшие морские пехотинцы, и те",
	"останавливались на 400 + 80, метре, прятали горящие сигареты в ладонях и",
	"замирали, прильнув к приборам ночного видения. А потом медленно, тихо отходили назад,",
	"не спуская глаз с туннеля и ни в коем случае не оборачиваясь к нему спиной. Дозор, в",
	"котором они были, стоял на ,200 + 50 метре , в 50+20 -70 +-+-++++ 50 метрах от",
	"пограничного столба. Но граница проверялась раз в день, и проверка уже закончилась",
	"несколько часов назад, и теперь их дозор был самым крайним, а за те часы, которые",
	"прошли со времени последней проверки, все твари, которых патруль мог спугнуть,",
	"наверняка снова начали подползать. Тянуло их как-то на огонек, поближе к людям.",
]


# Проверка корректности ввода пункта меню
def validate_integer(s):
	if s.isdigit():
		if 0 <= int(s) < 9:
			return True
		return False


# Вывод текста
def print_text(text):

	# Очищаем экран
	clear_screen()

	# Считаем ширину окна, в котором будет отображаться текст (viewer)
	width = max(len(x) for x in text)

	# Выводим границы viewer'a и предложения внутри
	print('_' * (width + 2))
	for line in text:
		print(('|{:<' + str(width) + '}|').format(line))

	print('-' * (width + 2))


# Функция для очистки экрана
def clear_screen():

	# Переводим курсор на в позицию (0, 0)
	print('\x1b[H')

	# Заполняем все использованное пространство пустыми символами
	for _ in range(30):
		print(' ' * 140, end='')

	# Возвращаем курсор в (0, 0)
	print('\x1b[H')


# Выводим меню
def print_menu():
	print('Выберите действие: ')
	print('1. Выровнять текст по левому краю')
	print('2. Выровнять текст по правому краю')
	print('3. Выровнять текст по ширине')
	print('4. Удалить все вхождения заданного слова')
	print('5. Заменить слово другим')
	print('6. Вычислить арифметические выражения (сложение и вычитание)')
	print('7. Найти самое длинное по количеству слов предложение и удалить его')
	print('8. Удалить все слова с заданным вхождением')
	print('0. Выйти из программы')
	print(' ' * 200, end='')


# Обрабатываем выбор пользователя
def get_choice():

	# Выводим меню и приглашение к вводу
	print_menu()
	print('\rВведите номер действия: ', end='')
	choice = input().strip()

	# Пока не получим корректный ввод, будем просить снова
	while not validate_integer(choice):
		clear_screen()
		print_text(text)
		print_menu()
		print('\rВведите корректный номер действия: ', end='')

		choice = input()

	return int(choice)


# Определяем текущее выравнивание
def check_align(text):
	if any(x[0] == ' ' and x[-1] == ' ' for x in text if len(set(x)) > 1):
		return 'width'

	if any(x[0] == ' ' for x in text if len(set(x)) > 1):
		return 'right'

	elif any('  ' in x for x in text if len(set(x)) > 1):
		return 'width'

	else:
		return 'left'


# Нормализуем текст
def normalize(text):

	# Идем построчно
	for i in range(len(text)):

		# Пропускаем пустые строки
		if len(text[i].split()) == 0: continue

		# Убираем все подряд идущие пробелы, если их больше одного
		text[i] = ' '.join([x for x in text[i].split(' ') if x != ''])

		# Приводим к корректному виду знаки пунктуации
		for c in punctuation:

			# Кроме / и *
			if c in '/*':
				continue
			text[i] = text[i].replace(f' {c}', f'{c}')\
				.replace(f'{c} ', f'{c}')

			text[i] = text[i][:-1].replace(f'{c}', f'{c} ') + text[i][-1]

		for sign in '+-':
			text[i] = text[i].replace(f'{sign} ', f'{sign}')


# Replace для списка 
def replace_list_el(lst, old, new):
	for i in range(len(lst)):
		if lst[i] == old:
			lst[i] = new

	return lst


# Удаляем слово из текста
def remove_word(text):
	clear_screen()
	print_text(text)
	print_menu()
	print('\rВведите слово, которое требуется удалить: ', end='')
	word = input().strip()
	if ' ' in word:
		return

	# Запоминаем текущее выравнивание
	align = check_align(text)

	# Считаем ширину viewer'a
	max_width = max(len(x) for x in text)

	# Проходимся по тексту
	for i in range(len(text)):

		# Бьем строку на слова
		words = text[i].split(' ')

		# И убираем все вхождения указанного слова
		if word in words:
			new_line = replace_list_el(words, word, '')

			# Если мы удалили все слова из строки, заполняем ее пробелами
			# под ширину viewer'a
			if len(new_line) == 1:
				text[i] = ' ' * max_width
			else:

				# Иначе просто склеиваем ее и записываем в список
				text[i] = ' '.join(new_line)

		# Все то же самое, только тут обрабатываются слова,
		# после которых идет какой-либо знак препинания
		for c in punctuation:
			if f'{word}{c}' in text[i].split(' '):
				new_line = replace_list_el(words, f'{word}{c}', f'{c}')
				if len(new_line) == 1:
					text[i] = ' ' * max_width
				else:
					text[i] = ' '.join(new_line)

	# Возвращаем выравнивание
	if align == 'left':
		align_left(text)

	elif align == 'right':
		align_right(text)

	else:
		align_width(text)


# Заменяем одно слово другим
def replace_word(text):
	clear_screen()
	print_text(text)
	print_menu()
	print('\rВведите два слова через пробел: ', end='')

	# Проверяем корректность ввода
	words = input().split()
	if len(words) != 2:
		print('\x1b[3B')
		for _ in range(4):
			print(' ' * 140)
		print('\x1b[4A')
		print('Ошибка ввода!')
		return
	word, new_word = map(str, words)

	# Запоминаем выравнивание
	align = check_align(text)

	# Аналогично, как с удалением, проходимся по строкам
	# разбиваем их на слова и заменяем
	for i in range(len(text)):
		line = text[i].split(' ')
		for j in range(len(line)):
			if word == line[j]:
				line[j] = new_word
			else:
				for c in punctuation:
					if f'{word}{c}' == line[j]:
						line[j] = f'{new_word}{c}'

		text[i] = ' '.join(line)

	# Возвращаем все на круги своя
	if align == 'left':
		align_left(text)

	elif align == 'right':
		align_right(text)

	else:
		align_width(text)


# Проверяем, является ли токен подходящим выражением
# Прим.: токен, в данном контексте, единица текста,
# отделенная от других пробелом
def check_for_expression(token):
	
	# Токен длиной < 3 не может быть подходящим выражением в нашем случае
	if len(token) < 3:
		return False

	# Убираем нулевой символ, если это знак
	if token[0] in '+-':
		token = token[1:]

	# Если нет + или -, значит это не выражение (или выражение, которое
	# нам не подходит)
	if not ('-' in token or '+' in token):
		return False

	return True


# Считаем выражение
def evaluate(token):

	punct = ''

	while token[-1] in ',.?!;:-()\'\" ':
		
		# Запоминаем пунктуацию, идущую после выражения	
		punct = token[-1] + punct
		
		# И удаляем ее
		token = token[:-1]

	# Приводим выражение в удобный вид
	token = token.replace('+', ' + ').replace('-', ' - ')
	operands = []
	operators = []
	remainder = ''
	splitted = token.split(' ')

	# Разбиваем выражение на операторы и операнды
	for k in range(len(splitted)):
		if splitted[k].isdigit():
			operands.append(int(splitted[k]))
		
		elif splitted[k] in '+-' and splitted[k - 1] not in '+-':
			operators.append(splitted[k])

		else:
			if len(splitted[k - 1:]) > 3:
				offset = 0
				for x in range(len(splitted[k - 1:])):
					if splitted[k - 1:][x].isdigit():
						offset = x - 1
						break

				if offset != 0:
					remainder = ''.join(splitted[k - 1:k + offset]) + \
					evaluate(''.join(splitted[k + offset:]))
			else:
				remainder = ''.join(splitted[k - 1:])
			break

	# Если операндов не оказалось, возвращаем исходный токен
	if len(operands) == 0: 
		return token + punct

	# Просчитываем выражение
	while len(operands) > 1:
		op0 = operands.pop(0)
		op1 = operands.pop(0)

		operator = operators.pop(0)

		if operator == '+':
			operands = [op0 + op1] + operands
		elif operator == '-':
			operands = [op0 - op1] + operands

	# Возвращаем посчитанное выражение
	return str(operands[0]) + remainder + punct


# Выполняем всю работу, связанную с просчетом математических операций
def calculate_expr(text):

	# Запоминаем выравнивание
	align = check_align(text)

	# Приводим текст к удобному виду
	normalize(text)

	# Проходимся по каждому слову и, если оно является подходящим выражением,
	# просчитываем его
	for i in range(len(text)):
		line = text[i]
		words = line.split(' ')
		for j in range(len(words)):
			word = words[j]
			if check_for_expression(word):
				result = evaluate(word)
				words[j] = result

		text[i] = ' '.join(words)

	# Возвращаем выравнивание
	if align == 'left':
		align_left(text)

	elif align == 'right':
		align_right(text)

	else:
		align_width(text)


# Переводим смещение из вида X символов от начала текста
# в вид i-ая строка, j-ый символ
def calculate_offset(text, offset):
	curr_pos = 0
	for i in range(len(text)):
		for j in range(len(text[i])):
			if curr_pos == offset:
				return i, j
			curr_pos += 1

	return -1, -1


# Собираем предложение, зная смещения начала и конца
def get_sentence(text, si, sj, ei, ej):

	# Берем кусочек первой строки
	sentence = text[si][sj:] + ' '

	# Если предложение заняло не одну строку, то забираем остальные,
	# не включая последнюю
	for i in range(si + 1, ei):
		for j in range(len(text[i])):
			sentence += text[i][j]
		sentence += ' '

	# Забираем кусочек последней строки
	sentence += text[ei][:ej + 1]
	sentence = sentence.strip()

	# Расставляем переносы строк, чтобы было удобнее читать в консоли
	ln = 0
	for i in range(0, len(sentence)):
		if sentence[i] == ' ' and ln > 100:
			sentence = sentence[:i] + '\n' + sentence[i + 1:]
			ln = -1
		ln += 1

	# Возвращаем
	if len(sentence) > 1:
		sentence = sentence.split('.')[0] + '.'
	
	return sentence


# Убираем предложение из текста
def remove_sentence(text, si, sj, ei, ej):
	
	# Считаем ширину viewer'a
	max_len = max(len(x) for x in text)

	# Меняем символы предложения на пробелы
	text[si] = text[si][:sj] + ' ' * (max_len - sj)

	for i in range(si + 1, ei):
		text[i] = ' ' * max_len

	text[ei] = ' ' * ej + text[ei][ej + 1:]



# Поиск и удаление самого длинного по кол-ву слов предложения
def find_and_delete(text):

	# Запоминаем выравнивание
	align = check_align(text)

	# Приводим текст к удобному виду
	normalize(text)

	start = 0
	end = 0
	words_cnt = 0
	curr_pos = 0

	max_words_cnt = 0
	longest_start = 0
	longest_end = 0

	# Ищем самое длинное по кол-ву слов предложение и запоминаем его начало и конец
	for i in range(len(text)):
		line = text[i].replace('...', '.')
		for j in range(len(line)):
			if line[j] == ' ' and line[j - 1] != '.':
				words_cnt += 1

			if line[j] in '.!?':
				words_cnt += 1
				end = curr_pos

				if words_cnt > max_words_cnt:
					max_words_cnt = words_cnt
					longest_start = start
					longest_end = end

				start = curr_pos + 1
				words_cnt = 0

			curr_pos += 1

		words_cnt += 1

	# Считаем для него смещения
	si, sj = calculate_offset(text, longest_start)
	ei, ej = calculate_offset(text, longest_end)

	# Получаем предложение по смещениям
	sentence = get_sentence(text, si, sj, ei, ej)

	# Удаляем его из текств
	remove_sentence(text, si, sj, ei, ej)

	# Выводим его в консоль
	print('\x1b[3B')
	for _ in range(4):
		print(' ' * 140)
	print('\x1b[4A')
	print(sentence)

	# Возвращаем выравнивание
	if align == 'left':
		align_left(text)

	elif align == 'right':
		align_right(text)

	else:
		align_width(text)


# Левое вырванивание
def align_left(text):
	normalize(text)
	for i in range(len(text)):
		text[i] = text[i].lstrip()


# Правое вырванивание
def align_right(text):
	normalize(text)
	max_width = max([len(x) for x in text])
	for i in range(len(text)):
		text[i] = ' ' * (max_width - len(text[i])) + text[i]


# Вырванивание по ширине
def align_width(text):

	# Нормализуем
	normalize(text)

	# Считаем ширину viewer'a
	max_width = max(len(x) for x in text)

	# Проходимся по каждой строке, кроме самой длинной
	for i in range(len(text)):
		if len(text[i]) == max_width:
			continue

		line = text[i]

		# Считаем необходимое кол-во пробелов, которое нужно вставить в строку
		words_cnt = len(line.split(' '))
		needed_spaces = max_width - len(line)
		space_len = 1

		# Вставляем пробелы
		if words_cnt == 1:
			needed_spaces = (max_width - len(line)) // 2
			line = ' ' * needed_spaces + line + ' ' * needed_spaces
			
		elif words_cnt != max_width + 1:
			while needed_spaces > words_cnt - 1:
				line = line.replace(' ' * space_len, ' ' * (space_len + 1))
				needed_spaces -= words_cnt - 1
				space_len += 1

			line = line.replace(' ' * space_len, ' ' * 
				(space_len + 1), needed_spaces)
		
		needed_spaces = 0
		text[i] = line


# Выходим из программы
def finish(text):
	sys.exit(0)


# Защита
def delete_word_with_ss(text):
	clear_screen()
	print_text(text)
	print_menu()
	print('\rВведите подпоследовательность, которая должна быть в удаляемых словах: ', end='')
	seq = input().strip()
	if ' ' in seq:
		return

	align = check_align(text)
	normalize(text)

	for i in range(len(text)):
		line = text[i].split()
		for word in line:
			if seq in word:
				line = replace_list_el(line, word, '') 

		text[i] = ' '.join(line)

	if align == 'left':
		align_left(text)

	elif align == 'right':
		align_right(text)

	else:
		align_width(text)


# Обрабатываем запрос пользователя
def process_task(id):
	tasks = [
		finish,
		align_left,
		align_right,
		align_width,
		remove_word,
		replace_word,
		calculate_expr,
		find_and_delete,
		delete_word_with_ss
	]

	tasks[id](text)


# Основная функция
def main():
	print('\x1b[?25l')
	normalize(text)
	while True:
		clear_screen()
		print_text(text)
		choice = get_choice()
		process_task(choice)


if __name__ == '__main__':
	main()

import string

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' + string.ascii_letters


def print_line(line):
	words = line.split()
	max_len = max(len(x) for x in words)

	for i in range(max_len):
		for w in words:
			if i < len(w):
				print(w[i], end=' ')
			else:
				print(' ', end=' ')
		print()

with open('in.txt', encoding='utf-8') as fin:
	with open('out.txt', 'w', encoding='utf-8') as fout:
		for line in fin:
			fout.write('------\n')

			words = line.split()
			max_len = max(len(x) for x in words)

			for i in range(max_len):
				for w in words:
					if i < len(w):
						fout.write(w[i])
					else:
						fout.write(' ')
				fout.write('\n')

with open('out.txt', encoding='utf-8') as fin:
	with open('out2.txt', 'w', encoding='utf-8') as fout:
		min_len = 1e18
		max_len = -1

		for line in fin:
			line_len = len([x for x in line if x.lower() in alphabet])

			min_len = min(min_len, line_len)
			max_len = max(max_len, line_len)

		min_len += min_len == 0
		fin.seek(0)

		for x in range(min_len, max_len + 1):
			for line in fin:
				line_len = len([x for x in line if x.lower() in alphabet])
				if line_len == x:
					fout.write(line)
			fin.seek(0)
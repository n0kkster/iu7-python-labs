from struct import *
import random

fmt = 'q'
size = calcsize(fmt)

def read_ind(f, index):
	f.seek(index * size)
	data = f.read(size)
	return unpack(fmt, data)[0]


def write_ind(f, index, data):
	f.seek(index * size)
	f.write(pack(fmt, data))


def print_file(f):
	f.seek(0)
	while (b := f.read(size)):
		print(unpack(fmt, b)[0])


# def insertion(lst):
# 	for i in range(len(lst)):
# 		j = i - 1
# 		key = lst[i]

# 		while lst[j] > key and j >= 0:
# 			lst[j + 1] = lst[j]
# 			j -= 1
# 		lst[j + 1] = key


# with open('nums.bin', 'rb+') as f:
# 	f.seek(0, 2)
# 	cnt = f.tell() // size
# 	f.seek(0)

# 	for i in range(1, cnt):
# 		j = i - 1
# 		key = read_ind(f, i)

# 		while j >= 0 and read_ind(f, j) > key:
# 			write_ind(f, j + 1, read_ind(f, j))
# 			j -= 1
# 		write_ind(f, j + 1, key)


with open('nums.bin', 'rb+') as f:
	f.seek(0, 2)
	cnt = f.tell() // size
	f.seek(0) 

	for i in range(cnt // 2):
		key = read_ind(f, i + cnt // 2)
		write_ind(f, i + cnt // 2, read_ind(f, i))
		write_ind(f, i, key)

	start = cnt // 2

	for i in range(start, 3 * cnt // 4):
		key = read_ind(f, i)
		# print(i, cnt - (i - start) - 1)
		write_ind(f, i, read_ind(f, cnt - i + start - 1))
		write_ind(f, cnt - i + start - 1, key)


	print_file(f)
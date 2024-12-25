len_1 = 0
len_2 = 0

with open('1.txt', 'r') as f:
	len_1 = len([x for x in f.readlines() if x])

with open('2.txt', 'r') as f:
	len_2 = len([x for x in f.readlines() if x])

with open('1.txt', 'r') as f1:
	with open('2.txt', 'r') as f2:

		min_file = f1
		min_len = len_1

		if len_2 < len_1:
			min_len = len_2
			min_file = f2


		with open('out.txt', 'w') as out:
			num1 = int(f1.readline().strip())
			num2 = int(f2.readline().strip())
			
			while True:
				if num1 <= num2:
					out.write(str(num1) + ' ')
					num1 = f1.readline().strip()
					if not num1: 
						break
					# print(num1)
					num1 = int(num1)
				else:
					out.write(str(num2) + ' ')
					num2 = f2.readline().strip()
					if not num2: 
						break
					# print(num2)
					num2 = int(num2)


			if min_file == f1:
				while (num := f2.readline().strip()):
					out.write(str(int(num)) + ' ')
			
			else:
				while (num := f1.readline().strip()):
					out.write(str(int(num)) + ' ')

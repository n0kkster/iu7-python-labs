from struct import *
import random

with open('nums.bin', 'wb') as f:
	with open('nums.txt', 'w') as f1:
		for i in range(8):
			# num = random.randint(-100000, 100000)
			num = i + 1
			f.write(pack('@q', num))
			f1.write(str(num) + ' ')
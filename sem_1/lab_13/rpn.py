operands = {"+": 1, "-": 1, "*": 2, "/": 2}

def convert(data):
	out, stack = [], []
	for i in range(len(data)):
		if data[i].isdigit():
			out.append(data[i])

		elif data[i] == "(":
			stack.append(data[i])

		elif data[i] == ")":
			for j in range(len(stack) - 1, -1, -1):
				if stack[j] == "(":
					stack.pop()
					break
				else:
					out.append(stack.pop())

		elif data[i] in operands:
			while stack != []:
				if stack[-1] != "(" and operands[data[i]] <= operands[stack[-1]]:
					out.append(stack.pop())
				else:
					break
			stack.append(data[i])
		else:
			return None
	return out + stack[::-1]


def calculate(rpn):
	while len(rpn) != 1:
		for i in range(2, len(rpn)):
			if rpn[i] in operands:
				rpn[i] = eval(str(rpn[i - 2]) + str(rpn[i]) + str(rpn[i - 1]))
				rpn = rpn[:i - 2] + rpn[i:]
				print(rpn)
				break
	return int(rpn[0])

rpn = convert('2 + 2 * 2'.strip().split())
print(rpn)
ans = calculate(rpn)
print(ans)
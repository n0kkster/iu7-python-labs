def flat(child, i = 0, parent = []):
	if i >= len(child) and parent == []:
		return []

	if i >= len(child):
		child = parent[i + 1:]
		parent = []
		return flat(child, 0, parent)

	if type(child[i]) is list:
		parent = child
		return flat(child[i], 0, parent)

	return [child[i]] + flat(child, i + 1, parent)


lst = [1, 2, 3, [4, 5, 6], 'ababa', 'dasdsadas', [32323, 'dasdsa', [], [232, 'avaav', [234, 76765], 67689890, ['badsjkba', 965788]]]]

print(flat(lst))
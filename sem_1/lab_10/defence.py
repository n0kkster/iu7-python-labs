lst = list(map(int, input().split()))

volume = 0
for i in range(1, len(lst) - 1):
	h = min(max(lst[:i]), max(lst[i + 1:]))
	if h >= lst[i]:
		volume += (h - lst[i])

print(volume)
from PIL import Image
import numpy as np

def average(p1, p2, p3, p4):
	average_red = (p1[0] + p2[0] + p3[0] + p4[0]) // 4 
	average_green = (p1[1] + p2[1] + p3[1] + p4[1]) // 4 
	average_blue = (p1[2] + p2[2] + p3[2] + p4[2]) // 4

	return (average_red, average_green, average_blue) 

def main():
	# path = input('Введите путь к изображению: ')
	path = 'sample.bmp'
	new_path = 'upscaled.bmp'

	if not path.endswith('.bmp'):
		print('Изображение должно быть в формате bmp.')
		return

	image = Image.open(path).convert('RGB')
	pixels = image.load()

	w, h = image.size

	upscaled_array = []

	for x in range(h):
		line = []
		for y in range(w):
			line.append(pixels[y, x])
			line.append((0, 0, 0))
		upscaled_array.append(line)
		upscaled_array.append([(0, 0, 0)] * 2 * w)

	for x in range(1, h * 2 - 1, 2):
		for y in range(1, w * 2 - 1, 2):
			upscaled_array[x][y] = average(upscaled_array[x - 1][y - 1], 
				upscaled_array[x - 1][y + 1], upscaled_array[x + 1][y - 1], 
				upscaled_array[x + 1][y + 1])

	for x in range(1, h * 2 - 1):
		for y in range((x + 1) % 2, w * 2 - 1, 2):
			upscaled_array[x][y] = average(upscaled_array[x - 1][y], 
					upscaled_array[x][y + 1], upscaled_array[x][y - 1], 
					upscaled_array[x + 1][y])

	for y in range(1, w * 2 - 1, 2):
		upscaled_array[0][y] = average(upscaled_array[0][y - 1], upscaled_array[0][y - 1], 
			upscaled_array[0][y + 1], upscaled_array[0][y + 1])

	for x in range(1, h * 2 - 1, 2):
		upscaled_array[x][0] = average(upscaled_array[x - 1][0], upscaled_array[x - 1][0], 
			upscaled_array[x + 1][0], upscaled_array[x + 1][0])

	for y in range((h - 1) % 2, w * 2 - 1, 2):
		upscaled_array[h][y] = average(upscaled_array[h][y - 1], upscaled_array[h][y - 1], 
			upscaled_array[h][y + 1], upscaled_array[h][y + 1])

	for x in range((w - 1) % 2, h * 2 - 1, 2):
		upscaled_array[x][w] = average(upscaled_array[x - 1][w], upscaled_array[x - 1][w], 
			upscaled_array[x + 1][w], upscaled_array[x + 1][w])

	upscaled_image = Image.fromarray(np.array(upscaled_array, dtype=np.uint8))
	upscaled_image.save(new_path)


if __name__ == '__main__':
	main()
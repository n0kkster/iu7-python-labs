from PIL import Image

MAGIC = 1488
MAGIC_LEN = 16


def write(offset, data, count, pixels, width):
	written = 0
	offset_pix, offset_channel = offset // 3, offset % 3

	if offset_channel != 0:
		x = offset_pix // width
		y = offset_pix % width
		curr_pixel = list(pixels[x, y])

		for i in range(offset_channel, 3):
			curr_pixel[i] = (curr_pixel[i] & ~1) | int(data[written])
			written += 1

		pixels[x, y] = tuple(curr_pixel)

		offset_channel = 0
		offset_pix += 1

	while written + 2 < count:
		x = offset_pix // width
		y = offset_pix % width
		curr_pixel = list(pixels[x, y])

		for i in range(len(curr_pixel)):
			curr_pixel[i] = (curr_pixel[i] & ~1) | int(data[written])
			written += 1

		pixels[x, y] = tuple(curr_pixel)
		offset_pix += 1

	remaining_bits = count - written

	x = offset_pix // width
	y = offset_pix % width
	curr_pixel = list(pixels[x, y])

	for i in range(remaining_bits):
		curr_pixel[i] = (curr_pixel[i] & ~1) | int(data[written])
		written += 1

	pixels[x, y] = tuple(curr_pixel)
	offset_channel += remaining_bits

	return offset_pix * 3 + offset_channel


def read(offset, pixels, count, width):
	bits = ''
	rc = 0
	offset_pix, offset_channel = offset // 3, offset % 3

	if offset_channel != 0:
		x = offset_pix // width
		y = offset_pix % width
		curr_pixel = pixels[x, y]

		for i in range(offset_channel, 3):
			bits += format(curr_pixel[i] & 1, '01b')
			rc += 1

		offset_channel = 0
		offset_pix += 1

	while rc + 2 < count:
		x = offset_pix // width
		y = offset_pix % width
		curr_pixel = pixels[x, y]

		for i in range(len(curr_pixel)):
			bits += format(curr_pixel[i] & 1, '01b')
			rc += 1

		offset_pix += 1

	remaining_bits = count - rc

	x = offset_pix // width
	y = offset_pix % width
	curr_pixel = pixels[x, y]

	for i in range(remaining_bits):
		bits += format(curr_pixel[i] & 1, '01b')
		rc += 1

	offset_channel += remaining_bits

	return bits, offset_pix * 3 + offset_channel


def encode(path, msg):
	image = Image.open(path).convert('RGB')
	pixels = image.load()
	max_length = image.width * image.height * 3 // 8
	offset = 0

	if len(msg) > max_length:
		return False, 'Сообщение слишком длинное!'

	bytes_seq = msg.encode('utf-8')
	msg_bits = ''.join([format(b, '08b') for b in bytes_seq])
	msg_len = len(msg_bits)
	len_bits = f'{msg_len:016b}'

	offset = write(offset, f'{MAGIC:016b}', MAGIC_LEN, pixels, image.width)
	offset = write(offset, len_bits, len(len_bits), pixels, image.width)
	write(offset, msg_bits, msg_len, pixels, image.width)

	image.save('encoded_image.bmp')

	return True, 'OK'


def decode(path):
	image = Image.open(path).convert('RGB')
	pixels = image.load()
	offset = 0

	magic, offset = read(offset, pixels, MAGIC_LEN, image.width)

	if int(magic, 2) != MAGIC:
		return False, 'Файл не содержит закодированного сообщения!'

	msg_len, offset = read(offset, pixels, 16, image.width)
	msg_len = int(msg_len, 2)

	bit_string, _ = read(offset, pixels, msg_len, image.width)
	bytes_seq = [int(bit_string[i:i+8], 2) for i in range(0, msg_len, 8)]
	message = bytes(bytes_seq).decode('utf-8')

	return True, message


if __name__ == '__main__':
	print('Вам стоит запустить frontend.py')

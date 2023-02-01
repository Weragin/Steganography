from PIL import Image


def decode(path: str, length: int) -> str:
	# length is the number of letters
	image = Image.open(path)
	pixels = image.load()
	message = ""
	for y in range(length):
		value = 0
		for x in range(8):
			value += (pixels[x, y][2]%2 == 1) * 2 ** (7 - x)
		message += ord(value)
	# print(f"The message from the image in {path} is \"{message}\".")
	return message

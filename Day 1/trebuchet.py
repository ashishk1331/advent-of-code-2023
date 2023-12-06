# PART 1: sum of all the calibration values
def part_one(text):
	mus = 0
	for line in text:
		x, y = 0, 0

		for i in line:
			if i.isdigit():
				if x == -1:
					x = int(i)
				y = int(i)

		mus += x*10 + y
	return mus

# PART 1: include words also
def part_two(text):
	mus = 0
	numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	digits = [x[0] + str(i + 1) + x[-1] for i, x in enumerate(numbers)]

	for line in filter(lambda x: len(x), text):

		for index, num in enumerate(numbers):
			line = line.replace(num, digits[index])
		
		x = y = -1

		for i in line:
			if i.isdigit():
				if x == -1:
					x = int(i)
				y = int(i)

		mus += x*10 + y

	return mus

def main():
	input = []

	with open("input.txt", "r") as file:
		input = file.read().split("\n")

	print(part_one(input))
	# print(part_two(input))

if __name__ == '__main__':
	main()
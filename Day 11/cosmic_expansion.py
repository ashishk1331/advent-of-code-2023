# PART 1: 
def part_one(data):
	dist = 0
	char = 49
	transformed_data = []
	for row in data.split("\n"):
		temp = []
		for each in row:
			if each == "#":
				temp.append(chr(char))
				char += 1
			else:
				temp.append(0)
		transformed_data.append(temp)

	adj = [[0]*(char - 49) for _ in range(char - 49)]

	for i in transformed_data:
		print(i)

	return dist

# PART 2: 
def part_two(data):
	pass

def main():
	input = []

	with open("input.txt", "r") as file:
		input = file.read()

	print("Part 1:", part_one(input))
	# print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()
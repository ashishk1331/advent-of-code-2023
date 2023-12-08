# PART 1: 
def part_one(data):
	pass

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
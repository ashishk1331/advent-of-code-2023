# PART 1: 
def part_one(data):
	count = 0

	res = []
	def backtrack():
		pass

	for line in data:
		print(line)


	return count

# PART 2: 
def part_two(data):
	pass

def main():
	data = []

	with open("input.txt", "r") as file:
		for line in file.read().split("\n"):
			x, y = line.split()
			data.append([x, tuple(map(int, y.split(",")))])

	print("Part 1:", part_one(data))
	# print("Part 2:", part_two(data))

if __name__ == '__main__':
	main()
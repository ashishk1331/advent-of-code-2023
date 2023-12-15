# PART 1: 
def part_one(data):
	data = [[data[i][j] for i in range(len(data))] for j in range(len(data[0]))]
	for slide in data:
		index, n = 0, len(slide)
		while index < n:
			if slide[index] == ".":
				next_o = index
				while next_o < n and slide[next_o] != "#":
					if slide[next_o] == "O":
						break
					next_o += 1
				if index < next_o < n and slide[next_o] == "O":
					slide[next_o], slide[index] = slide[index], slide[next_o]
			index += 1
	data = [[data[i][j]  for i in range(len(data))] for j in range(len(data[0]))]

	mus, index = 0, len(data)
	for row in data:
		count = sum([1 for x in row if x == "O"])
		mus += index * count
		index -= 1
	return mus

# PART 2: 
def part_two(data):
	pass

def main():
	data = []

	with open("input.txt", "r") as file:
		data = file.read().split("\n")

	print("Part 1:", part_one(data))
	# print("Part 2:", part_two(data))

if __name__ == '__main__':
	main()
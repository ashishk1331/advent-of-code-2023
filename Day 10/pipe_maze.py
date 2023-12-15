# PART 1: 
def part_one(data):
	start = None
	for i in range(len(data)):
		for j in range(len(data[0])):
			if data[i][j] == "S":
				start = [i, j]
				break
	directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]
	for each in directions:
		visited = set()
		path(data, start[0] + each[0], start[1] + each[1], visited)
	return start

GUIDE = {
	'|': [(0, -1), (0, 1)],
	'-': [(1, 0), (-1, 0)],
	'L': [(1, 0), (0, -1)],
	'J': [(0, 1), (-1, 0)],
	'7': [(-1, 0), (0, 1)],
	'F': [(0, 1), (1, 0)]
}

def path(matrix, row, col, visited):
	if 0 <= row < len(matrix) and 0 <= col < len(matrix[0]):
		
	

# PART 2: 
def part_two(data):
	pass

def main():
	input = []

	with open("input.txt", "r") as file:
		input = list(map(lambda x: [i for i in x], file.read().split("\n")))

	print("Part 1:", part_one(input))
	# print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()
def part_one(grid, start=(0, 0, 0, 1)):
	visited = set()
	rows, cols = len(grid), len(grid[0])
	stack = [start]

	while stack:
		(r, c, dx, dy) = stack.pop()
		if (
			r in range(rows) and
			c in range(cols) and
			(r, c, dx, dy) not in visited
		):
			visited.add((r, c, dx, dy))

			if grid[r][c] == '|' and dx == 0 and dy in [1, -1]:
				stack.append((r - 1, c, -1, 0))
				stack.append((r + 1, c, 1, 0))
			elif grid[r][c] == '-' and dx in [1, -1] and dy == 0:
				stack.append((r, c + 1, 0, 1))
				stack.append((r, c - 1, 0, -1))
			elif grid[r][c] == '\\':
				if (dx, dy) == (-1, 0):
					stack.append((r, c - 1, 0, -1))
				elif (dx, dy) == (0, 1):
					stack.append((r + 1, c, 1, 0))
				elif (dx, dy) == (1, 0):
					stack.append((r, c + 1, 0, 1))
				elif (dx, dy) == (0, -1):
					stack.append((r - 1, c, -1, 0))

			elif grid[r][c] == '/':
				if (dx, dy) == (-1, 0):
					stack.append((r, c + 1, 0, 1))
				elif (dx, dy) == (0, 1):
					stack.append((r - 1, c, -1, 0))
				elif (dx, dy) == (1, 0):
					stack.append((r, c - 1, 0, -1))
				elif (dx, dy) == (0, -1):
					stack.append((r + 1, c, 1, 0))
			else:
				stack.append((r + dx, c + dy, dx, dy))

	unique = set()
	for r, c, _, _ in visited:
		unique.add((r, c))
	return len(unique)

def part_two(grid):
	rows, cols = len(grid), len(grid[0])
	maxTiles = 0

	for i in range(rows):
		maxTiles = max(maxTiles, part_one(grid, (i, 0, 0, 1)), part_one(grid, (i, cols - 1, 0, -1)))

	for i in range(cols):
		maxTiles = max(maxTiles, part_one(grid, (0, i, 1, 0)), part_one(grid, (rows - 1, i, -1, 0)))

	return maxTiles

def main():
	data = []
	with open('input.txt', 'r') as file:
		for line in file.read().split('\n'):
			data.append([x for x in line])

	# print(part_one(data))
	print(part_two(data))

if __name__ == '__main__':
	main()
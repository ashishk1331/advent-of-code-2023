from math import lcm
from functools import reduce

# PART 1: count number of steps to reach to ZZZ
def part_one(direction, data):
	steps = 0
	index = 0
	n = len(direction)
	current = 'AAA'
	while current != 'ZZZ':
		steps += 1
		current = data[current][direction[index]]
		index = (index + 1)%n

	return steps

# PART 2: converge all node ending with A to all node ending with Z
def endpoint(arr):
	count = 0
	for i in arr:
		if i.endswith('Z'):
			count += 1
	return count == len(arr)

def part_two(direction, data):
	n = len(direction)
	start = [x for x in data if x.endswith('A')]
	end = [0]*len(start)
	for ind, point in enumerate(start):
		steps = 0
		index = 0
		while not point.endswith('Z'):
			point = data[point][direction[index]]
			steps += 1
			index = (index + 1)%n
		end[ind] = steps
	return reduce(lambda a, b: lcm(a, b), end)

def main():
	data = {}

	with open("input.txt", "r") as file:
		inp = file.read().split("\n")
		direction = inp.pop(0)
		inp.pop(0)
		for i in inp:
			src, dest = list(map(lambda x: x.strip(), i.split("=")))
			L, R = list(map(lambda x: x.strip(), dest.replace("(", "").replace(")", "").split(",")))
			data[src] = {
				'L': L,
				'R': R
			}

	print("Part 1:", part_one(direction, data))
	print("Part 2:", part_two(direction, data))

if __name__ == '__main__':
	main()
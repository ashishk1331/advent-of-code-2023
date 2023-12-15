# PART 1: next element of each series
def part_one(data):
	add = 0
	for seq in data:
		elem = seq[-1]
		while not sanity(seq):
			array = []
			for i in range(1, len(seq)):
				array.append(seq[i] - seq[i-1])
			elem += array[-1]
			seq = array
		add += elem
	return add

def sanity(arr):
	for i in arr:
		if i != 0:
			return False
	return True

# PART 2: previous element of each series
def part_two(data):
	add = 0
	for seq in data:
		m = seq[0]
		elem = 0
		while not sanity(seq):
			array = []
			for i in range(1, len(seq)):
				array.append(seq[i] - seq[i-1])
			seq = array
			elem += seq[0]
		add += m - elem
	return add

def main():
	data = []

	with open("input.txt", "r") as file:
		data = list(map(lambda x: list(map(int, x.split())), file.read().split("\n")))

	print("Part 1:", part_one(data))
	print("Part 2:", part_two(data))

if __name__ == '__main__':
	main()
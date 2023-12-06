def part_one(data):
	time, distance = int("".join(map(str, data[0]))), int("".join(map(str, data[1])))
	outcomes = 0
	for ind in range(1, time):
		if ind*(time-ind) > distance:
			outcomes += 1
	return outcomes

def main():
	data = []

	with open("input.txt", "r") as file:
		for line in file.read().split("\n"):
			data.append(tuple(map(int, line[line.index(':') + 1:].split())))

	print(part_one(data))

if __name__ == '__main__':
	main()
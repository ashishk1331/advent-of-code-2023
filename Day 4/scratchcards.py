def part_one(data):
	mus = 0
	for key, value in data.items():
		count = -1
		for i in value[0]:
			if i in value[1]:
				count += 1
		if count >= 0:
			mus += 2**count
	return mus

def part_two(data):
	dp = [1]*len(data)

	for card, numbers in data.items():
		matches = 0
		for i in numbers[0]:
			if i in numbers[1]:
				matches += 1
		for i in range(card, card + matches):
			dp[i] += dp[card - 1]
	return sum(dp)

def main():
	data = {}

	with open("input.txt", "r") as file:
		for line in file.read().split("\n"):
			key, value = line.split(":")
			key = int(key.split()[1])
			given, real = list(map(lambda x: tuple(map(int, x.split())), value.split("|")))
			data[key] = [given, real]

	# print(part_one(data))
	print(part_two(data))

if __name__ == '__main__':
	main()
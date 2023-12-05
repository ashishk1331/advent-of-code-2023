# I already did part one but it got lost in git resets ;_;
def part_one(data):
	return None

def part_two(data):
	return data

def main():
	data = None

	with open("input.txt", "r") as file:
		data = file.read().split("\n")

	# print(part_one(data))
	print(part_two(data))

if __name__ == '__main__':
	main()
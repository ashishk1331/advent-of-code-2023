# PART 1: sum hash value of each instruction
def part_one(data):
	value = 0
	for inst in data:
		current = 0
		for char in inst:
			current += ord(char)
			current *= 17
			current %= 256
		value += current
	return value

# PART 2: 256 box algorithm
def hash(inst):
	value = 0
	for char in inst:
		value += ord(char)
		value *= 17
		value %= 256
	return value

def part_two(data):
	boxes = [[] for _ in range(256)]
	for inst in data:
		# label, insert( or not), lens, label_hash
		label, insert = "".join([x for x in inst if x.isalpha()]), inst.find("=") > -1
		lens = int(inst[len(label) + 1:]) if insert else 0
		label_hash = hash(label)
		
		if insert:
			found = False
			for ind, box in enumerate(boxes[label_hash]):
				if box[0] == label:
					boxes[label_hash][ind][1] = lens
					found = True
					break
			if not found:
				boxes[label_hash].append([label, lens])
		else:
			for ind, box in enumerate(boxes[label_hash]):
				if box[0] == label:
					boxes[label_hash].pop(ind)

	mus = 0
	for index, box in enumerate(boxes):
		if len(box):
			for ind, [label, lens] in enumerate(box):
				mus += (index + 1)*( ind + 1 )* (lens)
	return mus

def main():
	data = []

	with open("input.txt", "r") as file:
		for x in file.read().split("\n"):
			data.extend(x.split(","))

	print("Part 1:", part_one(data))
	print("Part 2:", part_two(data))

if __name__ == '__main__':
	main()
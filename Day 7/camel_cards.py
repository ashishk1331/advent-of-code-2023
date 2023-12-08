# PART 1: amount of bid win
def hand_rank(hand):
	dmap = {}
	for i in hand:
		dmap[i] = dmap.get(i, 0) + 1
	count = tuple(sorted(dmap.values()))
	match count:
		case (1,): 
			return 7
		case (1, 4): 
			return 6
		case (2, 3): 
			return 5
		case (1, 1, 3): 
			return 4
		case (1, 2, 2): 
			return 3
		case (1, 1, 1, 2):
			return 2
		case (1, 1, 1, 1, 1):
			return 1
	return 0

def diff(one, two):
	dmap = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	for i in range(len(one)):
		delta = dmap.index(one[i]) - dmap.index(two[i])
		if delta < 0:
			return -1
		elif delta > 0:
			return 1
	return 0

def part_one(data):
	hands = [[] for _ in range(7)]

	for h in data:
		index = hand_rank(h[0]) - 1
		for ind, prev in enumerate(hands[index]):
			delta = diff(h[0], prev[0])
			if delta == 1:
				hands[index].insert(ind, h)
				break
		else:
			hands[index].append(h)

	mus = 0
	count = 1
	for i, arr in enumerate(filter(lambda x: len(x), hands)):
		for j, hand in enumerate(arr):
			mus += count*hand[1]
			count += 1

	return mus

# PART 2: now J comes in role

def hand_rank_two(hand):
	dmap = {}
	for i in hand:
		dmap[i] = dmap.get(i, 0) + 1
	if 'J' in dmap:
		dmap[max(dmap, key=dmap.get)] += dmap['J']
		del dmap['J']
	count = tuple(sorted(dmap.values()))
	match count:
		case (5, ):
			return 7
		case (1,): 
			return 7
		case (1, 4): 
			return 6
		case (2, 3): 
			return 5
		case (1, 1, 3): 
			return 4
		case (1, 2, 2): 
			return 3
		case (1, 1, 1, 2):
			return 2
		case (1, 1, 1, 1, 1):
			return 1
	return 0

def diff_two(one, two):
	dmap = ['J', 'A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
	for i in range(len(one)):
		delta = dmap.index(one[i]) - dmap.index(two[i])
		if delta < 0:
			return -1
		elif delta > 0:
			return 1
	return 0

def part_two(data):
	hands = [[] for _ in range(7)]

	for h in data:
		index = hand_rank_two(h[0]) - 1
		for ind, prev in enumerate(hands[index]):
			delta = diff_two(h[0], prev[0])
			if delta == 1:
				hands[index].insert(ind, h)
				break
		else:
			hands[index].append(h)

	mus = 0
	count = 1
	for _, bid in sum(filter(lambda x: len(x), hands), []):
			mus += count*bid
			count += 1

	return mus

def main():
	input = []

	with open("input.txt", "r") as file:
		input = list(map(lambda x: (x[0], int(x[1])), map(lambda x: x.split(), file.read().split("\n"))))

	print("Part 1:", part_one(input))
	print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()
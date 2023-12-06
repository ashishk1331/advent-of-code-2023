# I already did part one but it got lost in git resets ;_;
# because of the post where no input files should be shared in git repos
# What a drag!
def part_one(data):
	return None


def sweepLine(a, b):
	result = []
	while a and b:
		(p, q, r1), (r, s, r2) = a[0], b[0]
		start = max(p, r)
		end = min(q, s)
		if start <= end:
			result.append((start + r2, end + r2, r2))

		if q == s:
			a.pop(0)
			b.pop(0)
		elif q < s:
			a.pop(0)
		else:
			b.pop(0)

	result.extend(a)

	result = sorted(result, key=lambda x: x[0])

	return result


def part_two(data):
	all_maps = []

	# get all seeds
	seeds = data.pop(0)
	seeds = list(map(int, seeds[seeds.index(":")+1:].split()))
	temp = []
	for i in range(0, len(seeds), 2):
		temp.append((seeds[i], seeds[i] + seeds[i+1] - 1, 0))
	all_maps.append(sorted(temp, key=lambda x: x[0]))

	# trace all maps
	for pam in data:
		pam = pam.split("\n")
		pam.pop(0)
		ranges = []
		for i in pam:
			d, s, r = list(map(int, i.split()))
			ranges.append((s, s+r-1, d-s))
		ranges = sorted(ranges, key=lambda x: x[0])
		all_maps.append(ranges)

	# answer levels:
	# 0th = [(55, 67), (79, 92)]
	# 1st = [(57, 69), (81, 94)]
	# 2nd = [(57, 69), (81, 94)]
	# 3rd = [(53, 56), (61, 69), (81, 94)]
	# 4th = [(46, 49), (54, 62), (74, 87)]
	# 5th = [(45, 55), (78, 80), (82, 85), (90, 98)]
	# 6th = [(46, 56), (78, 80), (82, 85), (90, 98)]
	# 7th = [(46, 60), (82 ,84), (86, 89), (94, 98)]
	# answer = 46 <- 7th[0][0]

	x = all_maps[0]
	for i in range(1, len(all_maps)):
		x = sweepLine(x, all_maps[i])
		print([i[:2] for i in x])

	return x[0][0]


def main():
	data = None

	with open("input.txt", "r") as file:
		data = file.read().split("\n\n")

	# print(part_one(data))
	print(part_two(data))


if __name__ == '__main__':
	main()

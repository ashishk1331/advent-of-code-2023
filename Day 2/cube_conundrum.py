MAX = {
    'red': 12,
    'green': 13,
    'blue': 14
}

# PART 1: sum of all valid IDs


def part_one(data):
    count = 0
    for key, value in data.items():
        flag = True
        for subset in value:
            for color in subset:
                if color[0] > MAX[color[1]]:
                    flag = False
                    break
        if flag:
            count += int(key.split()[1])
    return count

# PART 2: calculate power of subsets of game


def part_two(data):
    mus = 0
    for key, value in data.items():
        minimum = {
            'red': 0,
            'green': 0,
            'blue': 0
        }
        for subset in value:
            for color in subset:
                minimum[color[1]] = max(minimum[color[1]], color[0])
        mus += minimum['red']*minimum['green']*minimum['blue']
    return mus


def main():
    input = None
    data = {}

    with open("input.txt", "r") as file:
        input = file.read().split("\n")
        for line in input:
            colon = line.index(":")
            key = line[:colon]
            value = line[colon + 1:].split(";")
            new_value = []
            for i in value:
                games = []
                for each in i.split(","):
                    x, y = each.split()
                    games.append((int(x), y))
                new_value.append(games)
            data[key] = new_value

    # print(part_one(data))
    print(part_two(data))


if __name__ == '__main__':
    main()

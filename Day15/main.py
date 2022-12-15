def readFile():
    with open("input.txt", "r", encoding="utf-8") as f:
        state = []

        for line in f:
            line = line.strip().split(" ")
            x = int(line[2].split("=")[-1].split(",")[0])
            y = int(line[3].split("=")[-1].split(":")[0])

            closest_x = int(line[-2].split("=")[-1].split(",")[0])
            closest_y = int(line[-1].split("=")[-1])

            state.append((x, y, closest_x, closest_y))
    return state


def distance(x, y, x2, y2):
    return abs(x - x2) + abs(y - y2)


def second_star(sensors):
    known = set((s[2], s[3]) for s in sensors)
    impossible = set()
    for sensor in sensors:
        (x, y, cx, cy) = sensor
        d = distance(x, y, cx, cy)

        curr_x = x
        dist = abs(y - 2000000)
        while dist <= d:
            impossible.add((curr_x, 2000000))
            curr_x -= 1
            dist += 1

        curr_x = x
        dist = abs(y - 2000000)
        while dist <= d:
            impossible.add((curr_x, 2000000))
            curr_x += 1
            dist += 1

    return len(impossible - known)


def part_two(sensors):
    for curr_y in range(4000000 + 1):
        ranges = []
        for sensor in sensors:
            (x, y, cx, cy) = sensor
            d = distance(x, y, cx, cy)
            dist = abs(y - curr_y)

            if d > dist:
                whats_left = d - dist
                s = max(0, x - whats_left)
                e = min(4000000, x + whats_left)
                ranges.append((s, e))

        # We want to check if there's any value that doesn't touch!
        last_end = 0
        for (s, e) in sorted(ranges):
            if last_end >= s:
                last_end = max(last_end, e)
            else:
                return (last_end + 1) * 4000000 + curr_y



if __name__ == "__main__":
    state = readFile()
    print(first_star(state))
    print(second_star(state))

#my code original was awful so I rewrite it, with help of reddit

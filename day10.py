import sys

def load_file(filename: str) -> list[str]:
    topmap: list[str] = []
    with open(filename, "r") as file:
        for line in file:
            topmap.append(line.strip('\n'))
    return topmap

HIKE_START = '0'
HIKE_END = '9'
DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Point = tuple[int, int]

def in_bounds(pos: Point, topmap: list[str]) -> bool:
    y, x = pos
    return 0 <= x < len(topmap[0]) and 0 <= y < len(topmap)

def find_tops_rec(topmap: list[str], curr: Point, found: set[Point]) -> None:
    y, x = curr
    if (topmap[y][x] == HIKE_END):
        found.add((y, x))
        return None

    for ny, nx in [(y+dy, x+dx) for dy, dx in DIRS]:
        if not in_bounds((ny, nx), topmap):
            continue

        if ord(topmap[y][x]) + 1 == ord(topmap[ny][nx]):
            find_tops_rec(topmap, (ny, nx), found)

def find_trailheads(topmap: list[str]) -> int:
    total: int = 0

    for y in range(len(topmap)):
        for x in range(len(topmap[0])):
            if topmap[y][x] != HIKE_START:
                continue

            found: set[Point] = set()
            find_tops_rec(topmap, (y, x), found)
            total += len(found)

    return total

def find_tops_rec_2(topmap: list[str], curr: Point) -> int:
    y, x = curr
    if (topmap[y][x] == HIKE_END):
        return 1

    total: int = 0
    for ny, nx in [(y+dy, x+dx) for dy, dx in DIRS]:
        if not in_bounds((ny, nx), topmap):
            continue

        if ord(topmap[y][x]) + 1 == ord(topmap[ny][nx]):
            total += find_tops_rec_2(topmap, (ny, nx))

    return total

def find_trailheads_2(topmap: list[str]) -> int:
    total: int = 0

    for y in range(len(topmap)):
        for x in range(len(topmap[0])):
            if topmap[y][x] != HIKE_START:
                continue

            total += find_tops_rec_2(topmap, (y, x))

    return total


def main(args) -> None:
    topmap: list[str] = load_file(args[0])

    print("Result 1:", find_trailheads(topmap))

    print("Result 2:", find_trailheads_2(topmap))


if __name__ == "__main__":
    main(sys.argv[1:])
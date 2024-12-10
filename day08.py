import sys

EMPTY = '.'
Point = tuple[int, int]
Antenas = list[Point]

def load_file(filename: str) -> list[str]:
    matrix: list[str] = []
    with open(filename, "r") as file:
        for line in file:
            matrix.append(line.strip('\n'))
    return matrix

def get_antenas(matrix: list[str]) -> dict[str, Antenas]:
    res: dict[str, Antenas] = {}

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if (matrix[y][x] == EMPTY):
                continue

            tmp: Antenas = res.get(matrix[y][x], [])
            tmp.append((y, x))
            res[matrix[y][x]] = tmp

    return res

def in_bounds(pos: Point, width: int, height: int) -> bool:
    y, x = pos
    return 0 <= x < width and 0 <= y < height

def count_antinodes(antenas: dict[str, Antenas], width: int, height: int) -> int:
    found: set[Point] = set()

    for _, positions in antenas.items():
        for idx, pos1 in enumerate(positions):
            for pos2 in positions[idx+1::]:
                y1, x1 = pos1
                y2, x2 = pos2

                dx: int = x2 - x1
                dy: int = y2 - y1

                antinode1: Point = (y1 - dy, x1 - dx)
                antinode2: Point = (y2 + dy, x2 + dx)

                if in_bounds(antinode1, width, height):
                    found.add(antinode1)

                if in_bounds(antinode2, width, height):
                    found.add(antinode2)
    return len(found)



def count_antinodes_2(antenas: dict[str, Antenas], width: int, height: int) -> int:
    found: set[Point] = set()

    for _, positions in antenas.items():
        for idx, pos1 in enumerate(positions):
            for pos2 in positions[idx+1::]:
                y1, x1 = pos1
                y2, x2 = pos2

                dx: int = x2 - x1
                dy: int = y2 - y1

                found.add(pos1)
                found.add(pos2)

                ay, ax = y1 - dy, x1 - dx
                while (in_bounds((ay, ax), width, height)):
                    found.add((ay, ax))
                    ay -= dy
                    ax -= dx


                ay, ax = y2 + dy, x2 + dx
                while (in_bounds((ay, ax), width, height)):
                    found.add((ay, ax))
                    ay += dy
                    ax += dx

    return len(found)


def main(args) -> None:
    matrix: list[str] = load_file(args[0])
    antenas: dict[str, Antenas] = get_antenas(matrix)

    print("Result 1:", count_antinodes(antenas, len(matrix[0]), len(matrix)))

    print("Result 2:", count_antinodes_2(antenas, len(matrix[0]), len(matrix)))


if __name__ == "__main__":
    main(sys.argv[1:])


import sys

def load_file(filename: str) -> list[list[str]]:
    matrix: list[list[str]] = []
    with open(filename, "r") as file:
        for line in file:
            matrix.append(list(line.strip('\n')))
    return matrix


EMPTY = '.'
BLOCK = '#'
VISITED = 'X'

Point = tuple[int, int]

def in_bounds(x: int, y: int, width: int, height: int) -> bool:
    return 0 <= x < width and 0 <= y < height

def fill_matrix(matrix: list[list[str]]) -> int:
    cnt: int = 0
    y: int = -1
    x: int = -1
    dir: Point = (0, -1)

    for i, row in enumerate(matrix):
        x = ''.join(row).find("^")
        if (x != -1):
            y = i
            break

    while True:
        if matrix[y][x] != VISITED:
            matrix[y][x] = VISITED
            cnt += 1

        dx, dy = dir
        nx, ny = x+dx, y+dy

        if not in_bounds(nx, ny, len(matrix[0]), len(matrix)):
            break

        if matrix[ny][nx] != BLOCK:
            x, y = nx, ny
            continue

        dir = (-dy, dx)

    return cnt



def find_loop_cnt(matrix: list[list[str]]) -> int:
    y: int = -1
    x: int = -1
    dir: Point = (0, -1)

    blocks: set[Point] = set()

    for i, row in enumerate(matrix):
        x = ''.join(row).find("^")
        if (x != -1):
            y = i
            break

    while True:
        dx, dy = dir
        nx, ny = x+dx, y+dy

        if not in_bounds(nx, ny, len(matrix[0]), len(matrix)):
            break

        if matrix[y][x] != VISITED:
            matrix[y][x] = VISITED
        elif matrix[ny][nx] == EMPTY:
            blocks.add((nx, ny))

        if matrix[ny][nx] != BLOCK:
            x, y = nx, ny
            continue

        dir = (-dy, dx)

    return len(blocks)


def main(args) -> None:
    matrix: list[list[str]] = load_file(args[0])
    res = fill_matrix(matrix)

    print("Result 1:", res)

    res = 0

    print("Result 2:", res)


if __name__ == "__main__":
    main(sys.argv[1:])


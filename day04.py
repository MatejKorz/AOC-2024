import sys

def load_file(filename: str) -> list[str]:
    res: list[str] = []
    with open(filename, "r") as file:
        for line in file:
            res.append(line.strip('\n'))

    return res

DIRS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
WORD_TO_FIND = "XMAS"

def in_bounds(x: int, y: int, height: int, width: int) -> bool:
    return 0 <= x < width and 0 <= y < height

def check_dirs(matrix: list[str], x: int, y: int):
    found: int = 0

    for dx, dy in DIRS:
        is_valid: bool = True
        for i in range(len(WORD_TO_FIND)):
            tx: int = x + dx*i
            ty: int = y + dy*i
            if not in_bounds(tx, ty, len(matrix), len(matrix[0])) or matrix[ty][tx] != WORD_TO_FIND[i]:
                is_valid = False
                break
        found += 1 if is_valid else 0

    return found

def find_occurences(matrix: list[str]) -> int:
    total: int = 0

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            total += check_dirs(matrix, x, y)

    return total

def find_occurences_2(matrix: list[str]) -> int:
    total: int = 0

    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            if (matrix[y][x] != 'A'):
                continue
            surround: str = ''.join([matrix[y+1][x-1], matrix[y+1][x+1], matrix[y-1][x+1], matrix[y-1][x-1]])
            if surround in {"SSMM", "MSSM", "MMSS", "SMMS"}:
                total += 1

    return total

def main(args) -> None:
    matrix = load_file(args[0])

    print("Result 1:", find_occurences(matrix))

    print("Result 2:", find_occurences_2(matrix))


if __name__ == "__main__":
    main(sys.argv[1:])


import sys

def load_file(filename: str) -> str:
    string: str
    with open(filename, "r") as file:
        string = file.read().strip('\n')
    return string

EMPTY = '.'

def transform_string(string: str, expanded: list[str]) -> None:
    id: int = 0
    for pos, char in enumerate(string):
        append_char: str = str(id) if pos % 2 == 0 else EMPTY
        for _ in range(int(char)):
            expanded.append(append_char)

        if (pos % 2 == 0):
            id += 1
    return None


def last_not_empty(back: int, expanded: list[str]) -> int:
    idx: int = back - 1

    while idx >= 0:
        if expanded[idx] != EMPTY:
            return idx

        idx -= 1
    return -1

def first_empty(front: int, expanded: list[str]) -> int:
    idx: int = front + 1

    while idx < len(expanded):
        if expanded[idx] == EMPTY:
            return idx
        idx += 1
    return len(expanded)


def move_blocks(expanded: list[str]) -> None:
    back_idx = last_not_empty(len(expanded), expanded)
    front_idx = first_empty(-1, expanded)

    while front_idx < back_idx:
        expanded[front_idx], expanded[back_idx] = expanded[back_idx], expanded[front_idx]
        back_idx = last_not_empty(back_idx, expanded)
        front_idx = first_empty(front_idx, expanded)

    return None

def compute_checksum(expanded: list[str]) -> int:
    checksum: int = 0
    for i, char in enumerate(expanded):
        if char == EMPTY:
            break
        checksum += i * int(char)
    return checksum


def main(args) -> None:
    disk_map: str = load_file(args[0])
    print(disk_map)
    disk_expanded: list[str] = []
    transform_string(disk_map, disk_expanded)
    print(''.join(disk_expanded))
    move_blocks(disk_expanded)
    print(''.join(disk_expanded))

    print("Result 1:", compute_checksum(disk_expanded))

    print("Result 2:", )


if __name__ == "__main__":
    main(sys.argv[1:])


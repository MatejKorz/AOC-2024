import sys

def load_file(filename: str) -> list[list[int]]:
    res: list[list[int]] = []
    with open(filename, "r") as file:
        for line in file:
            nums = [int(x) for x in line.split(" ") if x]
            res.append(nums)

    return res


def check_records(record: list[int]) -> int:
    is_asc: bool = record[0] < record[1]

    for i in range(len(record) - 1):
        if record[i] == record[i+1]:
            return 0
        if is_asc and record[i] > record[i+1]:
            return 0
        if not is_asc and record[i] < record[i+1]:
            return 0
        if not (1 <= abs(record[i] - record[i+1]) <= 3):
            return 0

    return 1


def main(args) -> None:
    matrix = load_file(args[0])

    total: int = 0
    for record in matrix:
        total += check_records(record)

    print("Result 1:", total)


    print("Result 2:")


if __name__ == "__main__":
    main(sys.argv[1:])


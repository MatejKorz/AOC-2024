import sys

Record = tuple[int, list[int]]


def load_file(filename: str) -> list[Record]:
    matrix: list[Record] = []
    with open(filename, "r") as file:
        for line in file:
            split_record = line.strip('\n').split(':')
            result: int = int(split_record[0])
            values: list[int] = [int(x) for x in split_record[1].strip().split(' ')]
            matrix.append((result, values))

    return matrix


def check_rec(result: int, curr: int, idx: int, values: list[int]) -> int:
    if len(values) <= idx or curr > result:
        return curr if result == curr else -1

    if check_rec(result, curr + values[idx], idx + 1, values) != -1:
        return result

    if check_rec(result, curr * values[idx], idx + 1, values) != -1:
        return result

    return -1

def is_possible(result: int, values: list[int]) -> bool:
    return check_rec(result, values[0], 1, values) == result

def check_records(records: list[Record]) -> int:
    total: int = 0

    for result, record in records:
        if is_possible(result, record):
            total += result

    return total



def check_rec_2(result: int, curr: int, idx: int, values: list[int]) -> int:
    if len(values) <= idx or curr > result:
        return curr if result == curr else -1

    if check_rec_2(result, curr + values[idx], idx + 1, values) != -1:
        return result

    if check_rec_2(result, curr * values[idx], idx + 1, values) != -1:
        return result

    combined: int = int(str(curr) + str(values[idx]))
    if check_rec_2(result, combined, idx + 1, values) != -1:
        return result

    return -1

def check_records_2(records: list[Record]) -> int:
    total: int = 0

    for result, record in records:
        if check_rec_2(result, record[0], 1, record) == result:
            total += result

    return total



def main(args) -> None:
    records: list[Record] = load_file(args[0])

    print("Result 1:", check_records(records))

    print("Result 2:", check_records_2(records))


if __name__ == "__main__":
    main(sys.argv[1:])


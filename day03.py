import sys

STR_CMD = "mul"

def load_file(filename: str) -> list[str]:
    res: list[str] = []
    with open(filename, "r") as file:
        for line in file:
            res.append(line)

    return res


def check_records(record: str) -> int:
    total: int = 0
    idx: int = 0
    while True:
        fidx = record.find(STR_CMD, idx)

        if (fidx == -1):
            break

        idx = fidx + 1

        start_idx: int = fidx + len(STR_CMD)
        if start_idx < len(record) and record[start_idx] == '(':
            end_idx = record.find(')', fidx, len(record))
            if end_idx == -1:
                continue
            inside: list[str] = record[start_idx+1:end_idx].split(',')
            if (len(inside) != 2):
                continue

            if (inside[0].isnumeric() and inside[1].isnumeric()):
                total += int(inside[0])*int(inside[1])

    return total


def check_records_2(record: str) -> int:
    total: int = 0
    idx: int = 0

    while True:
        fidx = record.find(STR_CMD, idx)

        if (fidx == -1):
            break

        disable_idx = record.find("don't()", idx)
        if (disable_idx != -1 and disable_idx < fidx):
            next_idx = record.find("do()", disable_idx)
            if (next_idx == -1):
                break
            else:
                idx = next_idx + 1
                continue

        idx = fidx + 1
        start_idx: int = fidx + len(STR_CMD)
        if start_idx < len(record) and record[start_idx] == '(':
            end_idx = record.find(')', fidx, len(record))
            if end_idx == -1:
                continue
            inside: list[str] = record[start_idx+1:end_idx].split(',')
            if (len(inside) != 2):
                continue

            if (inside[0].isnumeric() and inside[1].isnumeric()):
                total += int(inside[0])*int(inside[1])

    return total



def main(args) -> None:
    matrix = load_file(args[0])

    total: int = 0
    for record in matrix:
        total += check_records(record)

    print("Result 1:", total)


    total: int = 0
    total = check_records_2(''.join(matrix))

    print("Result 2:", total)


if __name__ == "__main__":
    main(sys.argv[1:])


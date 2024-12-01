import sys

def load_file(filename: str) -> tuple[list[int], list[int]]:
    left: list[int] = []
    right: list[int] = []
    with open(filename, "r") as file:
        for line in file:
            nums = [x for x in line.split(" ") if x]
            left.append(int(nums[0]))
            right.append(int(nums[1]))

    return left, right

def make_hist(lst: list[int]) -> dict[int, int]:
    res: dict[int, int] = dict()

    for elem in lst:
        cnt: int = res.get(elem, 0)
        res[elem] = cnt + 1

    return res

def main(args) -> None:
    (left, right) = load_file(args[0])

    left.sort()
    right.sort()

    total: int = 0
    for i in range(len(left)):
        total += abs(left[i] - right[i])

    print("Result 1:", total)

    hist: dict[int, int] = make_hist(right)
    total = 0
    for elem in left:
        total += elem * hist.get(elem, 0)

    print("Result 2:", total)


if __name__ == "__main__":
    main(sys.argv[1:])


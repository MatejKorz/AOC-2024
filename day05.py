import sys

def load_file(filename: str) -> tuple[dict[str, list[str]], list[list[str]]]:
    records: list[list[str]] = []
    rules: dict[str, list[str]] = {}
    with open(filename, "r") as file:
        while True:
            rule = file.readline().strip('\n').split("|")
            if len(rule) != 2:
                break
            tmp = rules.get(rule[0], [])
            tmp.append(rule[1])
            rules[rule[0]] = tmp

        while True:
            record = file.readline().strip('\n').split(',')
            if (record[0] == ''):
                break
            records.append(record)


    return rules, records


def check_record(rules: dict[str, list[str]], record: list[str]) -> int:
    found: set[str] = set()

    for elem in record:
        rule: list[str] = rules.get(elem, [])
        for rule_elem in rule:
            if (rule_elem in found):
                return 0
        found.add(elem)
    return int(record[len(record)//2])


def fix_record(rules: dict[str, list[str]], record: list[str]) -> int:
    for _ in range(len(record)):
        previous: list[str] = record.copy()
        previous.pop()

        for i in reversed(range(1, len(record))):
            elem: str = record[i]
            rule: list[str] = rules.get(elem, [])

            for rule_elem in rule:
                idx: int = -1

                for j in range(len(previous)):
                    if (previous[j] == rule_elem):
                        idx = j
                        break
                if (idx == -1):
                    continue
                record[i], record[idx] = record[idx], record[i]
            previous.pop()

    return int(record[len(record)//2])




def main(args) -> None:
    rules, records = load_file(args[0])
    res: int = 0
    for record in records:
        res += check_record(rules, record)

    print("Result 1:", res)

    res = 0
    for record in records:
        if (check_record(rules, record) == 0):
            res += fix_record(rules, record)

    print("Result 2:", res)


if __name__ == "__main__":
    main(sys.argv[1:])


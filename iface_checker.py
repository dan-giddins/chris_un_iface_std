import argparse
from prettytable import PrettyTable


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help="file to be parsed")
    # parser.add_argument('-a', '--audio', help="download audio only", action='store_true')
    # parser.add_argument('-c', '--custom_format', help="download a custom format")
    args = parser.parse_args()
    f = open(args.file, "r", encoding="utf8")
    header = f.readline()
    checked = [header.strip().split("|")]
    length = len(checked[0])
    print("Header length: " + str(length))
    errors = []
    i = 0
    for line in f:
        i += 1
        checked.append(line.strip().split("|"))
        if len(checked[i]) != length:
            print("Error: Line " + str(i + 1) + " is not the right length! (" + str(len(checked[i])) + ")")
            errors.append((checked[i]))
    checked[0].append("")
    table = PrettyTable(checked[0])
    errors = errors[:-1]
    for error in errors:
        table.add_row(error)
    print(table)


if __name__ == "__main__":
    main()

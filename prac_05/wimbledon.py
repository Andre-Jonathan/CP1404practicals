FILENAME = "wimbledon.csv"
records = []
with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for row in in_file:
        parts = row.strip().split(",")
        records.append(parts)

        print(row, end="")
print()

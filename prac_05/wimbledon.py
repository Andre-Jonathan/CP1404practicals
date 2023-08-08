FILENAME = "wimbledon.csv"
INCREMENT = 1
count = 0
records = []
libraries = {}

with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for row in in_file:
        parts = row.strip().split(",")
        records.append(parts)

print(records)
for i in records:
    del records[count][0], records[count][2:]
    count += INCREMENT
print(records)



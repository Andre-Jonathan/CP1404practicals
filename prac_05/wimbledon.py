"""
Emails
Estimate: 50 minutes
Actual:   106 minutes
"""
FILENAME = "wimbledon.csv"
SECOND_INDEX = 1
THIRD_INDEX = 2
INCREMENT = 1
count = 0
records = []
player_count = {}

with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for row in in_file:
        parts = row.strip().split(",")
        records.append(parts)


countries = [country[SECOND_INDEX] for country in records]

for name in records:
    try:
        player_count[name[THIRD_INDEX]] += INCREMENT
    except KeyError:
        player_count[name[THIRD_INDEX]] = INCREMENT

print("Wimbledon Champions:")
for player in player_count:
    print(f"{player} {player_count[player]}")
print()

print(f"These {len(set(countries))} countries have won Wimbledon:")
for country in set(countries):
    print(country, end=", ")

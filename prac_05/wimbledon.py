"""Time from 1:04 to 2:15
from 2:20 to 2:50
from 4:30 to 4:50"""

FILENAME = "wimbledon.csv"
INCREMENT = 1
count = 0
records = []
player_count = {}
with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
    in_file.readline()
    for row in in_file:
        parts = row.strip().split(",")
        records.append(parts)

print(records)
player_name = [entry[2] for entry in records]
print(set(player_name))

countries = [country[1] for country in records]
print(set(countries))

for name in records:
    try:
        player_count[name[2]] += INCREMENT
    except KeyError:
        player_count[name[2]] = INCREMENT

print(player_count)
print("Wimbledon Champions:")
for player in player_count:
    print(f"{player} {player_count[player]}")
print()

print(f"These {len(set(countries))} countries have won Wimbledon:")
for country in set(countries):
    print(country, end=", ")

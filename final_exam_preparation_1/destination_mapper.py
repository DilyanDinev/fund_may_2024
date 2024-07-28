import re

map_string = input()

pattern = r"(=|\/)([A-Z][A-Za-z]{2,})\1"

matches = re.findall(pattern, map_string)

destinations = [match[1] for match in matches]

travel_points = sum(len(destination) for destination in destinations)

print(f"Destinations: {', '.join(destinations)}\nTravel Points: {travel_points}")
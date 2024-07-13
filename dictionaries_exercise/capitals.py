# countries = input().split(", ")
# capitals = input().split(", ")
# final_dictionary = {countries[index]: capitals[index] for index in range(len(countries))}
# for country, capital in final_dictionary.items():
#     print(f"{country} -> {capital}")

countries = input().split(", ")
capitals = input().split(", ")
final_dictionary = dict(zip(countries, capitals))
for country, capital in final_dictionary.items():
    print(f"{country} -> {capital}")

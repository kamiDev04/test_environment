rivers = {'nile': 'egypt', 'volga': 'russia', 'rein': 'germany',}
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print('')
for river in rivers.keys():
    print(river.title())
print('')
for country in rivers.values():
    print(country.title())

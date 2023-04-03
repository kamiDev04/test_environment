cities = ['london', 'moscow', 'munich', 'belgorod', 'gamburg', 'berlin', 'new york']
print('The first three items in the list are:')
for city in cities [:3]:
    print(city)

print('\nThree items from the middle of the list are:')
for city in cities [2:5]:
    print(city)

print('\nThe last three items in the list are:')
for city in cities [-3:]:
    print(city)
jane = {'first_name': 'jane', 'last_name': 'spirina', 'age': 24, 'city': 'Moscow',}
nick = {'first_name': 'nick', 'last_name': 'reznikov', 'age': 27, 'city': 'Moscow',}
johnny = {'first_name': 'johnny', 'last_name': 'rudenko', 'age': 26, 'city': 'Belgorod',}
people = [jane, nick, johnny]
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name.title()}")

    print(f"\tAge: {person['age']}")

    location = person['city']
    print(f"\tCity: {person['city']}")
    print('')
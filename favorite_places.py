favorite_places = dict(jane=['moscow', 'kas', 'germany'], nick=['moscow', 'antalya', 'st. petersburg'],
                       johny=['n. novgorod', 'belgorod'])
for name, places in favorite_places.items():
    print(f"My friend {name.title()} like be in:")
    for place in places:
        print(f"\t{place.title()}")
    print('')
    
sparcle = {'name': 'sparcle', 'kind': 'cat', 'owner': 'bill'}
star = {'name': 'star', 'kind': 'dog', 'owner': 'john'}
betsy = {'name': 'betsy', 'kind': 'mini-pig', 'owner': 'catalina'}
mr_gold = {'name': 'mr_gold', 'kind': 'fish', 'owner': 'paulina'}
pets = [sparcle, star, betsy, mr_gold]
for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    name = pet['name']
    print(f"Look at the {name.title()}! This is {kind} of {owner.title()}!")
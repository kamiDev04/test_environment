pizzas = ['pepperoni', 'caprichosa', 'margarita', 'neopolitan', 'fetuchini']
friend_pizzas = pizzas[:]
pizzas.append('assorti')
friend_pizzas.append('green')
print(f'My favorite pizzas are:')
for pizza in pizzas:
    print(pizza.title())
print("\n My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza.title())

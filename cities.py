cities = {'moscow': {'country': 'russia', 'population': '12.6 million people', 'fact': 'Moscow’s oldest surviving building is more than 550 years old'},
    'new york': {'country': 'USA', 'population': '8.8 million people', 'fact': 'more than 800 languages are spoken in New York City, making it the most linguistically diverse city in the world. 4 in 10 households speak a language other than English'},
    'bangkok': {'country': 'Tailand', 'population': '8.2 million people', 'fact': 'Bangkok is Home to Red Bull'},
    }
for city, info in cities.items():
    print(f"A couple of things about {city.title()}:")
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"\tThis city based in {country.title()}.")
    print(f"\tHis population is {population}.")
    print(f"\tAnd very interesting fact: {fact}.")
    print('')

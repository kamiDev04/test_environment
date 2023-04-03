responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is you name?\n")
    response = input(f"OK, {name.title()}! Where are you want to be on your holidays?\n")
    responses[name] = response
    repeat = input(f"So, {name.title()}. Would you like to let another person respond?")
    if repeat == 'no':
        polling_active = False

print('\n---- Poll result ----')
for name, response in responses.items():
    print(f"{name.title()} be like in {response.title()}!")
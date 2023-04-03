hello = "\nHello there! Please, add your toping."
hello +="\n(Enter 'quit' for finish)"

active = True
while active:
    topping = input(hello)
    if topping == 'quit':
        active = False
    else:
        print(f'topping {topping.title()} has been added')
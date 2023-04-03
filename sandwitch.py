sandwich_orders = ['pastrami', 'classic', 'neapolitan', 'pastrami', 'green', 'fish', 'pastrami']
finished_sandwiches = []
print("OK. Let's cook!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Now, we cooked {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nAll sandwiches has been finished:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich.title()} sandwich")
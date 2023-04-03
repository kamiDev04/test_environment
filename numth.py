numbers = []
for number in range(1, 10):
    if number == 1:
        number = f'{number}st'
        numbers.append(number)
    elif number == 2:
        number = f'{number}nd'
        numbers.append(number)
    elif number == 3:
        number = f'{number}rd'
        numbers.append(number)
    else:
        number = f'{number}th'
        numbers.append(number)
for number in numbers:
    print(number)
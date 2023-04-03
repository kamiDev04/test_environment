print('Напиши число, а я скажу, кратно оно 10 или нет.')
number = input()
number = int(number)
if number % 10 == 0:
    print(f'Число {number} кратно 10.')
else:
    print(f'Число {number} не кратно 10.')
print('На сколько персон вы бы хотели заказать столик?')
table = input()
table = int(table)
if table > 8:
    print('Извините, придётся подождать')
else:
    print('Всё ок, залетай, братишка!!')


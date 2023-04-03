names = ['эйнштейн', 'моррис', 'буш']
message_1 = f'Уважаемый, {names[0].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_2 = f'Уважаемый, {names[1].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_3 = f'Уважаемый, {names[2].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
print(message_1)
print(message_2)
print(message_3)
print(len(names))

name_del = 'моррис'
names.remove(name_del)

print(len(names))

print(name_del)
names.append('Себастьян')
message_1 = f'Уважаемый, {names[0].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_2 = f'Уважаемый, {names[1].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_3 = f'Уважаемый, {names[2].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
print(message_1)
print(message_2)
print(message_3)
print(len(names))

print('Нужно больше гостей!!!!')
names.insert(0, 'Дружок')
names.insert(2, 'Петушок')
names.append('Корешок')
message_1 = f'Уважаемый, {names[0].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_2 = f'Уважаемый, {names[1].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_3 = f'Уважаемый, {names[2].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_4 = f'Уважаемый, {names[3].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_5 = f'Уважаемый, {names[4].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
message_6 = f'Уважаемый, {names[5].title()}! Пожалуйста, приходите ко мне на обед в 6:00'
print(message_1)
print(message_2)
print(message_3)
print(message_4)
print(message_5)
print(message_6)
print(len(names))

print('Ох, к сожалению, придёт только 2 гостя')
name_sorry_0 = names.pop(0)
print(f'Сорян, {name_sorry_0.title()}(( не приходи.')
name_sorry_1 = names.pop(1)
print(f'Сорян, {name_sorry_1.title()}(( не приходи.')
name_sorry_3 = names.pop(3)
print(f'Сорян, {name_sorry_3.title()}(( не приходи.')
name_sorry_2 = names.pop(2)
print(f'Сорян, {name_sorry_2.title()}(( не приходи.')
name_yes_1 = names[0]
print(f'Эй, чувак, {name_yes_1.title()}. Если что, все в силе, приходи')
name_yes_2 = names[1]
print(f'Эй, чувак, {name_yes_2.title()}. Если что, все в силе, приходи')
print(len(names))
del names[0]
del names[0]
print(names)

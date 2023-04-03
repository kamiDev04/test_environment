favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['jen', 'john', 'sarah', 'edward', 'phil', 'michael']
for men in people:
    if men in favorite_languages.keys():
        print(f"Thank you, {men.title()} for your vote!")
    else:
        print(f"Come on, {men.title()}! Give me your vote!")
        
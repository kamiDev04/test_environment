def sandwich(*elements):
    print(f'My sandwich have:')
    for element in elements:
        print('\t', element.title())

sandwich('meat', 'beef', 'cucumber')
    
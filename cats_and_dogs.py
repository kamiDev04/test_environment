filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        pass
        # print(f'File {filename} not found.')
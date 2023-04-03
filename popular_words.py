import os
for root, dirs, files in os.walk(".."):
    for filename in files:
        print(filename)


# for filename in filenames:
#     try:
#         with open(filename, encoding='utf-8') as f:
#             contents = f.read()
#             print(contents)
#     except FileNotFoundError:
#         print(f'File {filename} not found.')
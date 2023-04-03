users = ['john', 'nick', 'lara', 'admin', 'master']
if users:
    for user in users:
        if user == 'admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for login again.')
else:
    print('We need to ind some users!')

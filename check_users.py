current_users = ['john', 'nick', 'Lara', 'admin', 'master']
current_users_low = []
for current_user in current_users:
    current_users_low.append(current_user.lower())
new_users = ['John', 'bill', 'jack', 'LARA', 'mickael']
for new_user in new_users:
    if new_user.lower() in current_users_low:
        print('Please, change your name')
    else:
        print('Name is available')
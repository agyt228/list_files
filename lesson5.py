'''f = open('users.txt', 'r')
users_new = []
users = f.readlines()
for user in users:
    users_new.append(user.replace('\n', ''))

print(users_new)
f.close()
f = open('users.txt', '')
f.write('\nuser8:12345:700')
f.close()
'''
'''users = ['user1', 'user2', 'user3'] #список (list)
users[0] = 'user4'
a = (4, 5, 6, 7, 4) #кортеж неизменяемые (tuple)
user = {'name': 'User1', 'age': 22}
user['name']'''
#[{'login': 'user1', 'password': '12345', 'balance': 100},{'login': 'user1', 'password': '12345', 'balance': 100},{'login': 'user1', 'password': '12345', 'balance': 100}]

def parseusers():
    f = open('users.txt', 'r')
    users_new = []
    users = f.readlines()
    for user in users:
        user_t = user.replace('\n', '')
        user_n = user_t.split(':')
        users_new.append({
            'login': user_n[0],
            'password': user_n[1],
            'balance': int(user_n[2])
        })
    f.close()
    return users_new

def setbalanceuser(login, balance):
    users = parseusers()
    users_new = []
    for user in users:
        if user['login'] == login:
            users_new.append({'login': user['login'], 'password': user['password'], 'balance': balance})
        else:
            users_new.append({'login': user['login'], 'password': user['password'], 'balance': user['balance']})
    f = open('users.txt', 'w')
    for user in users_new:
        f.write(user['login'] + ':' + user['password'] + ':' +str(user['balance'] )+ '\n')
#дз узнать где ошибка
import time
while True:
    login = input('login: ')
    password = input('password: ')
    for user in parseusers():
        if login == user['login'] and password == user['password']:
            balance = int(input('balance: '))
            if balance > user['balance']:
                print('error balance')
                time.sleep(5)
                break
            else:
                print(f'balance: {user['balance'] - balance}')
                setbalanceuser(login, user['balance'] - balance)
                time.sleep(5)


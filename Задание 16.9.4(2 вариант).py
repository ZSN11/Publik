
clients = []

while 'y':
    client = []
    name = input('¬ведите им€ нового клиента''  ')
    client.append(name)
    second_name = input('¬ведите фамилию нового клиента''  ')
    client.append(second_name)
    citi = input('¬ведите город проживани€ нового клиента''  ')
    client.append(citi)
    balance = input('¬ведите баланс нового клиента (руб)''  ')
    client.append(balance)
    clients.extend([client])
    stop = input("введите y,если продолжить или n, если остановитьс€"  ' ')

    if stop == 'y':
     continue
    else:
     break

for c in clients:
     print(*c, sep=",  ")

clients = []

while 'y':
    client = []
    name = input('������� ��� ������ �������''  ')
    client.append(name)
    second_name = input('������� ������� ������ �������''  ')
    client.append(second_name)
    citi = input('������� ����� ���������� ������ �������''  ')
    client.append(citi)
    balance = input('������� ������ ������ ������� (���)''  ')
    client.append(balance)
    clients.extend([client])
    stop = input("������� y,���� ���������� ��� n, ���� ������������"  ' ')

    if stop == 'y':
     continue
    else:
     break

for c in clients:
     print(*c, sep=",  ")
a = int(input("Введите число покупаемых билетов"))
b = int(input("Введите число посетителей в возрасте 18 - 25 лет"))
c = int(input("Введите число посетителей в возрасте старше 25 лет"))
if (b + c) > a:
    print("Вы не правильно ввели число покупаемых билетов")
else:
    if a <= 3:
     d = b * 990 + c * 1390
    else:
     d = (b * 990 + c * 1390) * 0.9
print("Сумма к оплате", d)
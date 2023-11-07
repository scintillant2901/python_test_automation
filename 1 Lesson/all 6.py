x = int(input()) #Сколько у Вас денег?
a = 30 #хлеб
b = 50 #молоко
c = 100 #сыр
d = a + b + c #общая стоимость товаров
e = x - d #сумма сдачи
if e >= 0:
    if e > 0:
        print('Стоимость товаров:', d, 'руб')
        print('Ваша сдача:', e, 'руб')
    else:
        print('Спасибо, что без сдачи!')
else:
    print('Недостаточно денег')


cash = int(input('Сколько у вас денег? '))

bread = 30
milk = 50
cheese = 100
total_price = bread + milk + cheese

if total_price < cash:
print('Стоимость товаров ' + str(total_price) + ' руб.')
change = cash - total_price
print('Ваша сдача ' + str(change) + ' руб.')
elif total_price == cash:
print('Спасибо, что без сдачи!')
else:
print('Недостаточно денег')
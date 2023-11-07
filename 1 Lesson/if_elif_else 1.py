'''Первый вариант'''
x = int(input())
y = int(input())
if x + y > 10:
    print('Сумма больше')
elif x + y < 10:
    print('Сумма меньше')
else:
    print('Сумма равна')

'''Второй вариант с использованием else'''
x = int(input())
y = int(input())
if x + y > 10:
    print('Сумма больше')
else:
  if x + y < 10:
      print('Сумма меньше')
  else:
      print('Сумма равна')
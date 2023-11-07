x = int(input())
y = int(input())
z = int(input())
if x <= z <= y:
    print('Это нормально')
elif z < x:
    print('Слишком мало бегаете')
else:
    print('Много бегать вредно')

'''Second ver'''
X = int(input())
Y = int(input())
Z = int(input())

if Y >= Z >= X:
print("Это нормально")
elif Z > Y:
print("Много бегать вредно")
elif Z < X:
print("Слишком мало бегаете")
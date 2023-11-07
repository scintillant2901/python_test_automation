'''Первый вариант'''
a,b,c,d = False, True, False, True
print((a and b) and (not c or d))

'''Второй вариант'''
a,b,c,d = False, True, False, True
print(a and ((b and not c) or d))
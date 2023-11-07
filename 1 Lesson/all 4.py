a = int(input())
b = int(input())
c = int(input())
if a > b:
    if b > c:
        print(b)
    elif a > c:
        print(c)
    else:
        print(a)
else:
    if c > b:
        print(b)
    elif c < a:
        print(a)
    else:
        print(c)
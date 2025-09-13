count = 0
f = True
while f == True:
    a = input()
    b = input('')
    c = input()

    a = int(a)
    c = int(c)

    if b == '+':
        r = a + c
        print(r)
    elif b == '-':
        r = a - c
        print(r)
    elif b == '*':
        r = a*c
        print(r)
    elif b == '/':
        r = int(a/c)
        print(r)
    else:
        print('error')
    count += 1
    if count == 10:
        f = False
    
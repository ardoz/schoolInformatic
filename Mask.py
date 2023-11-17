line1 = input()
be = '?'
nbe = '*'
if (be in line1 or nbe in line1) and ' ' not in line1 :
    print('Возможно маска')
else:
    print('Нет, это не маска!')
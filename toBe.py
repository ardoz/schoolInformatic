line1 = input()
line2 = input()
be = 'Быть'
nbe = 'Не быть'

def findWord(string, word):
    result=False;
    if word in string:
        result = True;
    return result

if (findWord(line1, be) and findWord(line2, be)) or (findWord(line1, nbe) and findWord(line2, nbe)):
    print('Выбор сделан!')
elif (findWord(line1, nbe) and findWord(line2, be)) or (findWord(line1, be) and findWord(line2, nbe)):
    print('Вот в чём вопрос!')
else:
    print('Определитесь!')
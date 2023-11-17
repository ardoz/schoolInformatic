try:
    time = int(input())
    if time in range(-1, 5) or time == 23:
        print("Ночь")
    elif time in range(4, 11):
        print("Утро")
    elif time in range(10, 18):
        print("День")
    elif time in range(17, 23):
        print("Вечер")
    else:
        print("Ошибка")
except ValueError:
    print("Ошибка")
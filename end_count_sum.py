total = 0

while True:
    user = input('Введите число или слово "Стоп" для выхода\n')
    if user.isalpha():
        if user == 'Стоп' or user == 'стоп':
            print('Сумма: ',total)
            break
        else:
            print('Ошибка ввода')
    else:
        total += int(user)

from random import randint

comp = randint(1,15)
attempts = 0

print('Угадайте число от 1 до 15, у вас 5 попыток\n')

while True:
    
    user = int(input('Введите ваше число\n'))
    
    if attempts == 5:
        print('Увы, вы проиграли.\n')
        break
    
    if user == 'Выход':
        print('Вы вышли из игры\n')
        break
    
    if user == comp:
        print('Победа!\n')
        break
    
    if user < comp:
        print('Ваше число меньше загаданного')
        attempts += 1
        
    if user > comp:
        print('Ваше число больше загаданного')
        attempts += 1

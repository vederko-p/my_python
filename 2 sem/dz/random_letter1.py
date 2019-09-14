import random

l = ['питон','пары','утро']

def random_word(l):
    return l[random.randint(0,len(l)-1)]

compword = random_word(l)

def random_letter(l):
    return random.choice(compword)

completter = random_letter(compword)

def index_of_completter(compword,completter):
    return list(compword).index(completter)

indexofcompletter = index_of_completter(compword,completter)

word2 = list(compword)
list2 = list(word2)
list2[indexofcompletter] = '?'
word2 = ''.join(list2)

print(word2)

user = str(input('Введите букву \n'))

if user == completter:
    print('Победа!\nСлово: ' + compword)
else:
    print('Увы! Попробуйте в другой раз\nСлово: ' + compword)

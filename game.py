import random

class battle:
    
    count = 0

    
    def __init__(self,name='player'): #создание персонажа
        self._stats=[100,[1,0],0,10,[0,0,0]] #статы, [здоровье,скорость,броня,патроны,усиления]
        battle.count += 1
        self._name = name
        self._position = [0,0]
        print('Добро пожаловать в битву, {0}!'.format(self._name))


    def get_stats(self): #получение характеристик персонажа
        print('Характеристики игрока {0}:\nЗдоровье - {1}\nСкорость - {2}\nБроня - {3}\nПатроны - {4}\nУсиления - Броня:{5}, Ускорение:{6}, Аптечка:{7}'.format(self._name,self._stats[0],self._stats[1][0],self._stats[2],self._stats[3],self._stats[4][0],self._stats[4][1],self._stats[4][2]))

    def get_position(self): #получение позиции персонажа
        print('Позиция игрока {0} - {1}'.format(self._name,self._position))


    def shot(self,pers2): #выстрел
        r = random.randint(0,1)
        self._stats[2] += -1
        if pers2._stats[2] != 0: #если у атакуемого персонажа есть броня, при попадании снимется она, а не здоровье
            pers2._stats[2] += -1
        else:
            pers2._stats[0] += -5*r
        print('Игрок {0}, выстрелил и{2} попал в игрока {1}'.format(self._name,pers2._name,' не' * (1-r)))
        
    def search(self): #поиск предметов
        _t = random.randint(0,5)
        _tools = ['броню','ускорение','аптечку','патроны','пустой ящик с патронами','поврежденную броню','пустую консервную банку']
        if _t <= 2:
            self._stats[4][_t] += 1
        elif _t == 3:
            self._stats[3] += random.randint (1,5)
        self._position[0] += 1
        self._position[1] += -1
        print('Игрок {0} нашел - {1}'.format(self._name,_tools[_t]))


    def use_aid(self): #использование аптечки
        self._stats[0] += 3
        self._stats[4][2] += -1
        print('Игрок {0} использовал аптечку'.format(self._name))
        self._position[0] += 1 #анимация*
        self._position[1] += -1 #анимация*

    def use_speed(self): #использование ускорения
        self._stats[1][0] += 1
        self._stats[1][1] += 3
        self._stats[4][1] += -1
        self._position[0] += 1 #анимация*
        self._position[1] += -1 #анимация*
        print('Игрок {0} использовал ускорение'.format(self._name))

    def use_armor(self): #использование брони
        self._stats[2] += 1
        self._stats[4][0] += -1
        self._position[0] += 1 #анимация*
        self._position[1] += -1 #анимация*
        print('Игрок {0} использовал броню'.format(self._name))

        
    def move(self): #передвижение
        if self._stats[1][0] == 1: #если у персонада нет ускорения, он будет двигаться медленно
            self._position[0] += 5
            self._position[1] += 5
        elif self._stats[1][0] != 1: #если ускорение есть, персонаж будет двигаться быстрее
            self._position[0] += 15
            self._position[1] += 15
            if self._stats[1][1] == 0: #ускорение дается лишь на время, с каждым ходом, действие ускорения заканчивается
                self._stats[1][0] += -1
            else:
                self._stats[1][1] += -1
            


print('создаем новых игроков:')
pers1 = battle()
pers2 = battle('воитель')

print('смотрим статистику:')
pers1.get_stats()

print('стреляем в другого игрока:')
pers1.shot(pers2)
print('статистика атакуемого игрока:')
pers2.get_stats()

print('ищем предметы:')
pers1.search()

print('можем применить что-нибудь из имеющихся усилителей, use_aid, use_soeed, use_armor')

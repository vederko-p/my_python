s = 'У лукоморья 123 дуб зеленый 456'

if s.count('я') != 0:
    print ("1) Индекс буквы 'я' - {0}".format(str(s.index('я'))))
    
print("2) Буква 'у' встречается {0} раза".format(s.count('у')))

if s.isalpha():
    print('3) no way')
else:
    print('3) ' + s.upper())

if len(s) > 4:
    print('4) ' + s.lower())

print('5) ' + 'О' + s[1:])

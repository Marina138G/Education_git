import random
print ('Сейчас будет сгенерирован список случайных чисел.')
def spisok ():
    t = []
    while len(t) < 10:
        r = random.randint(0,100)
        if r not in t:
            t.append(r)
    return (t)
sp = spisok()
print (sp)
def zamena (s):
    m = max(s)
    n = int(input(f'Введите любое число от 0 до {m}: \n'))
    for i in s:
        if i == m:
            z = s.index(i)
            s.pop(z)
            s.insert(z,n)
    print(f'Программа удачно заменила {m} на {n}')
    print(f'Новый список: \n{s}')
zamena (sp)
import random
print ('Сейчас будет сгенерирован список случайных чисел.')
def spisok ():
    t = []
    while len(t) < 10:
        r = random.randint(0,100)
        if r not in t:
            t.append(r)
    return (t)
#print (spisok())
sp = spisok()
print (sp)
def zamena (s):
    ss = sorted(s)
    m = ss [-1]
    n = int(input(f'Введите любое число от 0 до {m}: \n'))
    ss[-1] = n
    print (ss)
    print(f'Программа удачно заменила {m} на {n}')
zamena (sp)
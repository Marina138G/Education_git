def donats (sn, sm):
    e = {}
    e.setdefault(sn, sm)
    return e
print('Поступления от донатов\nДобавьте доната')
surname = str(input('Никнейм: '))
sump = int(input("Сумма (грн.): "))
donats(surname, sump)
entry = donats(surname, sump)
i = 0
while i == 0:
    q = input('Добавить ещё одного доната?(Да - 1/Нет - 0): ')
    if q == '1':
        surname = str(input('Никнейм: '))
        sump = int(input("Сумма (грн.): "))
        donats(surname, sump)
        entry.update(donats(surname, sump))
        i += 0
    elif q == '0':
        print('Список донатов')
        for key, value in entry.items():
            print (key, ' - ', value, 'грн.')
        se = sum(entry.values())
        ae = len (entry)
        print(entry)
        print (f'Задонатили {ae} человек(ка).\nСобрано {se} грн.')
        i += 1
    elif q == '':
        print('Необходимо сделать выбор')
        i += 0
    else:
        print('Необходимо сделать корректный выбор')
        i += 0





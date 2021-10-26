import random
t = []
while len(t) < 10:
    r = random.randint(0,10)
    if r not in t:
        t.append(r)
print (t)
def find(a):
    if a in t:
        print('Число ' + str(a) + ' находится в списке под номером ' + str(t.index(a)))
    else:
        print(f'Число {a} отсутствует в списке')
        number = int(input("Укажи другое число, которое необходимо найти: \n"))
        find(number)
number = int(input("Укажи число, которое необходимо найти: \n"))
find(number)
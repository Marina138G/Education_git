import random
def lotereya (f, s):
    loto = []
    i = 0
    for i in range(0, 10):
        loto.append(random.randint(f, s))
        i += 1
    print(loto)
    print("Отсортированный список\n", sorted(loto))
    print("Уникальные значения\n", set(loto))
print("Создание списка случайных чисел")
a = int(input("Выбери минимальное число: \n"))
b = int(input("Выбери максимальное число: \n"))
lotereya(a, b)
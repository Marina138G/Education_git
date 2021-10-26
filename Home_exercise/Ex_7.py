def workout(a, b, l):
    i = 1
    while a < b:
        print(f"Подход #{i}")
        a += l
        i+=1
        if b-a == 0:
            break
        print(f"Осталось ещё {b-a}")
    print(f"Поздравляем! Вы выполнили упражнение {ex}. Переходим к следующему.")
ex = input("Какое упражнение будем выполнять? - ")
tt = int(input("Сколько раз - "))
s = int(input("Сколько подходов - "))
st = int(tt/s)
print(f"Необходимо сделать {s} подхода(ов) по {st} раз(а)")
print("Начинаем!")
workout(0, tt, st)


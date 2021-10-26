num = (input(("Введи число -  ")))
def cut_sum (a):
    s = []
    s.extend(a)
    s2 = [int(n) for n in s]
#print(s2) - список элементов типа "integer"
#print(list(map(int, s))) - то же самое, только через "map"
    return(sum(s2))
print(f'Сумма элементов числа: {cut_sum (num)}')

def sumnum(x):
n=0
for i in range(len(x)):
    n+=int(x[i])
    return n
c = sumnum(input())
print('Сумма', c)
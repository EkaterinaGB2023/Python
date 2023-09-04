'''Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)'''
from random import randint

min_value = int(input('Введите минимальное значение диапазона:'))
max_value = int(input('Введите максимальное значение диапазона:'))
n = int(input('Введите количество элементов начального списка :'))
lst = [randint(-5,11) for i in range(n)]
print(lst)
lst_ind = []

for i in range(len(lst)):
    if lst[i] >= min_value and lst[i] <= max_value:
        # print(i, end = ' ')   если не создавать новый список, то можно их просто таким образом выводить
        lst_ind.append(i)
print(lst_ind)

# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сделать без встроенных ф-ций, например, get_dummies?
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
columne_name_1 = "whoAmI_" + lst[0] # определяем название столбца 1
columne_name_2 = "whoAmI_" + lst[len(lst)-1] # определяем название столбца 2
print(columne_name_1) # проверяем корректность создания имени столбца 1
print(columne_name_2) # проверяем корректность создания имени столбца 2
random.shuffle(lst) # перемешиваем значения в списке
new_lst_1 = []
new_lst_2 = []
for item in lst: # заполняем новый список №1 1 и 0
    if item == lst[0]:
        new_lst_1.append(1)
    else:
        new_lst_1.append(0)

for item in lst: # заполняем новый список №2 1 и 0
    if item == lst[len(lst)-1]:
        new_lst_2.append(1)
    else:
        new_lst_2.append(0)

data = pd.DataFrame({'whoAmI': lst})
print(data)
# Раскомментируйте строки 30, 31 для сравнения Data Frame и таблицы, созданной вручную
# to_one_hot = pd.get_dummies(data, columns=['whoAmI'])
# print(to_one_hot)

new_data = pd.DataFrame({columne_name_1: new_lst_1, columne_name_2: new_lst_2})
print(new_data)

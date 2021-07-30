"""
Объединение (слияние) или пересечение сортированных
списков
Есть два сортированных списка (массива).
Нужно написать функцию, которая делает новый сортированный список с
объединением или пересечением элементов этих двух списков
(два варианта задачи, выберите любой или оба сразу).
Пример:
1-ый список: 1, 2, 2, 5, 7, 14
2-й список: 4, 6, 6, 7, 9, 14, 15
Объединение: 1, 2, 2, 4, 5, 6, 6, 7, 7, 9, 14, 14, 15 Пересечение: 7, 14
"""
x = list(map(int, input().split(',')))
y = list(map(int, input().split(',')))
z = set(x)
z.intersection_update(y)
print(z)
x.extend(y)
x.sort()
print(x)

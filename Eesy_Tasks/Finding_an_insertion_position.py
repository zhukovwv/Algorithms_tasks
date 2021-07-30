"""
Дан список чисел и целевое число.
Найдите индекс целевого числа, если оно есть в списке, а если нету,
то верните его в конец списка.
"""

x = list(map(int, input().split(',')))
y = int(input())
try:
    print(x.index(y))
except ValueError:
    print(len(x))

"""
Содержит дубликат
Дан массив чисел. Если в нем есть дубликаты, то верните True, если нет, то False.

Sample Input:

    1,2,3,1
Sample Output:

    True
"""

x = list(map(int, input().split(',')))
y = list(set(x))
if y == x:
    print(False)
else:
    print(True)

"""
Соедините два отсортированных списка
Объедините два отсортированных связанных списка и
верните его в виде отсортированного списка.
Список должен быть составлен путем сращивания узлов первых двух списков.

Sample Input:

    1,2,4
    1,3,4
Sample Output:

    [1, 1, 2, 3, 4, 4]
"""

x = list(map(int, input().split(',')))
y = list(map(int, input().split(',')))
x.extend(y)
x.sort()
print(x)

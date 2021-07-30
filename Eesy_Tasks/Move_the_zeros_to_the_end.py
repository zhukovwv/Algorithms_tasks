"""
Подвинь нули в конец
Дан массив чисел nums. Найди в этом массиве нули
и подвинь их в конец. Остальные числа должны идти в том же порядке.

Sample Input:

    0,1,3,12
Sample Output:

    [1, 3, 12, 0]
"""

a = list(map(int, input().split(',')))

x = [i for i in a if i != 0]
y = [i for i in a if i == 0]
x.extend(y)
print(x)

"""
Часто повторяемый
Данн список чисел nums размером n.

Верните самый часто повторяемый элемент из списка.
Часто повторяемый это элемент, который появляется больше чем [n/2]

Sample Input:

    3,2,3
Sample Output:

    3
"""

x = list(map(int, input().split(',')))
count = int(0)
top = int(0)
idm = None

for i in x:
    for j in x:
        if i ==j:
            count += 1
    if count > top and count > len(x)/2:
        top = count
        idm = i
    count = 0


print(idm)

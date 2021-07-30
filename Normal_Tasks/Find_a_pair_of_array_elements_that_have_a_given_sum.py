"""
Найти пару элементов массива,
имеющих заданную сумму
Дан массив на входе, необходимо определить,
есть ли в нем пара чисел, имеющая заданную сумму.
"""

x = sorted(set(list(map(int, input().split(' ')))))
n = int(input())
check = False
for i in range(len(x)):
    if check is True:
        break
    for j in range(len(x)-1):
        if x[i] + x[j+1] == n:
            check = True
            break
print(x)
print(check)

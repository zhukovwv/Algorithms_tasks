"""
Первый уникальный символ в строке
Дана строка. Найдите первый неповторяющийся символ в этой строке и верните его индекс. Если такого элемента нет, то верните -1.

Sample Input:

    leetcode
Sample Output:

    0
"""
s = input()
print(list(map(s.count, s)).index(1) if s and 1 in list(map(s.count, s)) else -1)

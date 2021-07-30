"""
Повторяемая подстрока
Дана строка, проверьте, может ли она состоять из повторяющихся подстрок.

Sample Input:

    abab
Sample Output:

    True
"""
s = input()
print((s+s)[1:-1].find(s) != -1)

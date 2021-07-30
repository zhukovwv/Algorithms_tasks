"""
Бинарная сумма
Даны 2 двоичных числа. Верните их сумму в двоичной системе счисления.

Sample Input:

    11
    1
Sample Output:

    100
"""

a = input()
b = input()
print(bin(int(a, 2) + int(b, 2))[2:])

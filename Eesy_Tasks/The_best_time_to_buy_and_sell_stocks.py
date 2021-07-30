"""
Лучшее время для покупки и продажи акций
Вам дан массив цен price, где price[i] цена на i+1 день.

Вы хотите увеличить вашу выгоду выбрав один день чтобы купить
акцию и выбрать один день в будущем чтобы ее продать.

Верните максимальную выгоду. Если вы не можете получить выгоду, то верните 0.

Например дан массив цен [7,1,5,3,6,4]. Покупая на второй день по цене 1,
вы можете выгодно продать акцию на  5 день по цене 6. 6 - 1 = выгода равна 5.

Sample Input:

    7,1,5,3,6,4

Sample Output:

    5
"""

price = [int(i) for i in  input().split(',') if i.isnumeric()]


def f(price):
    mi = min(price)
    nind = price.index(mi) + 1
    if len(price) <= nind:
        return '0'
    sl = price[nind::]
    ma = max(sl)
    if ma > mi:
        return str(ma - mi)
    else:
        return '0'


print(f(price))

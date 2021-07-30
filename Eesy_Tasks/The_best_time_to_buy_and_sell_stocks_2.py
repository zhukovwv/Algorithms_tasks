"""
Лучшее время для покупки и продажи акций II
Вам дан массив цен price, где price[i] цена на i+1 день.

Вы хотите увеличить вашу выгоду выбрав один день чтобы
купить акцию по выгодной цене и выбрать столько дней
сколько возможно чтобы продать и купить заного для получения максимальной выгоды.

Верните максимальную выгоду. Если вы не можете получить выгоду, то верните 0.

Например дан массив цен [7,1,5,3,6,4].
Покупая на второй день по цене 1, вы можете выгодно
продать акцию на 3 день по цене 5. Выгода 5 - 1 = 4.
Затем еще раз купить на 4й день по цене 3 и
продать по цене 6. Выгода 6 - 3 = 3.
Итоговая выгода 4 + 3 = 7.

Sample Input:

7,1,5,3,6,4
Sample Output:

7
"""

prices = [int(i) for i in  input().split(',')]
if len(prices) == 0:
    print(0)
minnum = prices[0]
profits = []
maxflag = False
for i in range(1,len(prices)):
    if prices[i]<prices[i-1]:
        if maxflag:
            profit = maxnum - minnum
            profits.append(profit)
            maxflag = False
        minnum = prices[i]
        maxflag = False
    if prices[i] > prices[i-1]:
        maxflag = True
        maxnum = prices[i]
if maxflag:
    profit = maxnum - minnum
    profits.append(profit)
if profits == []:
    print(0)
else: print(sum(profits))

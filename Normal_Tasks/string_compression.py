"""
Сжатие строки
Дана строка (возможно, пустая), состоящая из букв A-Z:

AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB

Нужно написать функцию RLE, которая на выходе даст строку вида:

A4B3C2XYZD4E3F3A6B28

И сгенерирует ошибку, если на вход пришла невалидная строка.
Если символ встречается 1 раз, он остается без изменений,
Если символ повторяется более 1 раза, к нему добавляется количество повторений.
"""


def rle(word):
    word_new = list()
    count = int(1)
    word += " "
    for i in range(len(word)-1):
        tmp = word[i+1]
        if word[i] == tmp:
            word.replace(word[i+1], "")
            count += 1
            continue
        if count == 1:
            word_new += word[i]
            count = 1
        if count > 1:
            word_new += word[i] + str(count)
            count = 1
    return word_new


x = input()
check = "A4B3C2XYZD4E3F3A6B28"
print("".join(map(str, rle(x))))
print("".join(map(str, rle(x))) == check)

"""
Удаление дубликатов из отсортированного массива
Дан отсортированный массив nums, удалите в нем дубликаты так,
чтобы в результирующем массиве каждый элемент появлялся только один раз.

Sample Input:

    1,1,2
Sample Output:

    [1, 2]
"""

nums = map(int, input().split(','))
print(list(set(nums)))

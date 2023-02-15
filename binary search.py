# бинарный поиск

nums = [2, 4, 6, 8, 1, 3, 5, 7, 9]
nums.sort()  # сортируем
print(nums)

search_for = 5  # что ищем

lowest = 0
highest = len(nums) - 1
index = None  # будущий индекс искомого элемента

while (lowest <= highest) and (index is None):
    # повторяем пока не найдено
    mid = (lowest + highest) // 2  # середина

    if nums[mid] == search_for:
        # нашли по середине
        index = mid
    else:
        if search_for < nums[mid]:
            # ищем в левой части списка (среза)
            highest = mid - 1
        else:
            # ищем в правой  списка (среза)
            lowest = mid + 1

print('Искомый элемент', search_for, 'найден под индексом', index)
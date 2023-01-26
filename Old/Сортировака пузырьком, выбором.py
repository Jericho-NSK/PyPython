a = [4, 5, 2, 8, 3, 45, 67, 4, 453]


# bubble sort_while
# i = 0
# while i < len(a) - 1:
#     j = 0
#     while j < len(a) - i - 1:
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
#         j += 1
#     i += 1
# print("bubble sort_while : ", a)


# bubble sort_for
# def bubble_sort(arr):
#     n = len(arr)
#     for j in range(n):
#         for i in range(0, n - j - 1):
#             q = arr[i + 1]
#             if arr[i] > q:
#                 arr[i], q = q, arr[i]

#
#
# bubble_sort(a)
# print("bubble sort_for: ", a)

# selection sort_while
# i = 0  # В цикле переменная i хранит индекс ячейки, в которую записывается минимальный элемент. Сначала это будет первая ячейка.
# while i < len(a) - 1:  # len(a) - 1, так как последний элемент обменивать уже не надо.
#     smallest = i  # ПОИСК МИНИМУМА. Сначала надо найти минимальное значение на срезе от i до конца списка.
#     # Переменная m будет хранить индекс ячейки с минимальным значением. Сначала предполагаем, что в ячейке i содержится минимальный элемент.
#     j = i + 1  # Поиск начинаем с ячейки следующей за i.
#     while j < len(a):
#         if a[j] < a[smallest]:  # будем сравнивать значение ячейки j, со значением ячейки m.
#             smallest = j  # Если в j значение меньше, чем в m, сохраним в m номер найденного на данный момент минимума.
#         j += 1  # Перейдем к следующей ячейке.
#     a[i], a[smallest] = a[smallest], a[i]  # ОБМЕН ЗНАЧЕНИЙ. В ячейку i записывается найденный минимум, а значение из ячейки i переносится на старое место минимума.
#     i += 1  # ПЕРЕХОД К СЛЕДУЮЩЕЙ НЕОБРАБОТАННОЙ ЯЧЕЙКЕ
# print(a)


# selection sort_for and while
# def sel_sort(array):
#     for i in range(len(array) - 1):
#         smallest = i
#         j = i + 1
#         while j < len(array):
#             if array[j] < array[smallest]:
#                 smallest = j
#             j = j + 1
#         array[i], array[smallest] = array[smallest], array[i]
#
#
# sel_sort(a)
# print(a)


# selection sort_for
def selection_sort(array):
    for i in range(len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]


selection_sort(a)
print(a)

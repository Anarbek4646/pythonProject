def bubble_sort(arr):
    n = len(arr)
    for i in range(n):

        swapped = False

        for j in range(0, n - i - 1):
            # Сравниваем соседние элементы
            if arr[j] > arr[j + 1]:
                # Меняем элементы местами
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True


        if not swapped:
            break


my_list = [64, 34, 25, 12, 22, 11, 90]
print("Исходный список:", my_list)

bubble_sort(my_list)
print("Отсортированный список:", my_list)
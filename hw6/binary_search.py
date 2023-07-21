def binary_search(arr, target):
    ResultOk = False
    First = 0
    Last = len(arr) - 1
    while First < Last:
        Middle = (First+Last) // 2
        if target == arr[Middle]:
            First = Middle
            Last = First
            ResultOk = True
            Pos = Middle
        else:
            if(target > arr[Middle]):
                First = Middle+1
            else:
                Last = Middle-1
    if ResultOk == True:
        return f'Элемент найден под индексом: {Pos}'
    else:
        return 'Элемент не найден в данном списке'



my_sorted_list = [1,2,3,4,5,6,8,9,10,11]

target_value = 10
print(binary_search(my_sorted_list, target_value))



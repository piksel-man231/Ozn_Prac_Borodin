# Написать функцию order_weight, которая сортирует список положительных чисел.
# Критерий сортировки - возрастание веса числа (сумма всех цифр числа).
# Если два числа имеют одинаковый вес, сортировать их так, словно они строки.
#
# Примеры:
# [56, 65, 74, 100, 99, 68, 86, 180, 90] ==>
# [100, 180, 90, 56, 65, 74, 68, 86, 99]


import traceback


def order_weight(integers):

    min = 10000000000000000000
    min_index = 0
    new_list = list()
    while len(integers) != 0:
        
        i = len(integers)
        for j in range(0, i-1):
            z = 0
            while z < len(integers):
                temp_int = 0
                temp_str = str(integers[j])
                mass = 0

                for h in range(0, len(temp_str)):
                    mass += int(temp_str[h])

                    if mass < min:
                        min = mass
                        min_index = j
                z += 1    
        temp_int = int(integers[min_index])
        integers.pop(min_index)
        new_list.append(temp_int)
    integers = new_list
    print (integers)
# Тесты
try:
    assert order_weight([103, 123, 4444, 99, 2000]) == [2000, 103, 123, 4444, 99]
    assert order_weight([2000, 10003, 1234000, 44444444, 9999, 11, 11, 22, 123]) == [11, 11, 2000, 10003, 22, 123, 1234000, 44444444, 9999]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
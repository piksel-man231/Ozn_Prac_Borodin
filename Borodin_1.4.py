# Написать функцию order_weight, которая сортирует список положительных чисел.
# Критерий сортировки - возрастание веса числа (сумма всех цифр числа).
# Если два числа имеют одинаковый вес, сортировать их так, словно они строки.
#
# Примеры
# [56, 65, 74, 100, 99, 68, 86, 180, 90] ==>
# [100, 180, 90, 56, 65, 74, 68, 86, 99]

hui = [10, 22, 8888888888]
sum = 0
min = 1000000000000000000000
for i in hui:
    while i > 0:
        sum += i % 10
        i = int(i/10)
    
    if sum < min:
        min = sum

    print(sum) 
    sum = 0

print(min)
    


#import traceback


def order_weight(integers):
    pass
    

'''   
# Тесты
try:
    assert order_weight([103, 123, 4444, 99, 2000]) == [2000, 103, 123, 4444, 99]
    assert order_weight([2000, 10003, 1234000, 44444444, 9999, 11, 11, 22, 123]) == [11, 11, 2000, 10003, 22, 123, 1234000, 44444444, 9999]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
'''
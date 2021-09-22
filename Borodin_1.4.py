import traceback


def order_weight(integers):
    #массив для веса чисел
    weight_integers = []
    #вспомогательная переме
    sum = 0
    
    #считаем сумму числа и добавляем в массив
    for i in integers:
        while i > 0:
            sum += i % 10
            i = int(i/10)
    
        weight_integers.append(sum)
        sum = 0

    # определяем длину массива
    Len = len(weight_integers)
    #Внешний цикл, количество проходов N-1
    for i in range(Len):
        # Внутренний цикл, N-i-1 проходов
        for j in range(0, Len-i-1):
            #если элементы меньше то меняем их местами
            if weight_integers[j] > weight_integers[j+1]:
                weight_integers[j], weight_integers[j+1] = weight_integers[j+1], weight_integers[j]
                integers[j], integers[j+1] = integers[j+1], integers[j]
            #если элементы равны, сравниваем числа как строки
            elif weight_integers[j] == weight_integers[j+1]:
                if str(integers[j]) > str(integers[j+1]):
                    weight_integers[j], weight_integers[j+1] = weight_integers[j+1], weight_integers[j]
                    integers[j], integers[j+1] = integers[j+1], integers[j]
                    
    return integers
    
# Тесты
try:
    assert order_weight([103, 123, 4444, 99, 2000]) == [2000, 103, 123, 4444, 99]
    assert order_weight([2000, 10003, 1234000, 44444444, 9999, 11, 11, 22, 123]) == [11, 11, 2000, 10003, 22, 123, 1234000, 44444444, 9999]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

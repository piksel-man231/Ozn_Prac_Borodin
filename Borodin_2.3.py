# Написать функцию next_version, которая будет принимать строку (текущая версия программного обеспечения)
# и будет возвращать строку, содержащую следующий номер версии.
# Правила:
# все числа, кроме первого, должны быть меньше 10
# если после увеличения они становятся равными 10 - установите их в 0 и последовательно увеличите следующий номер
#
# Пример:
# next_version("1.2.3") ==> "1.2.4"
# next_version("0.9.9") ==> "1.0.0"


import traceback



def next_version(s):
    #разбиваем строку на список
    versionList = (s.split('.'))
    #переводим список строк в список чисел
    versionList = list(map(int, versionList))
    #переворачиваем список для прохода с конца
    versionList = versionList[::-1]
    
    #проходимся по всему списку
    for index, number in enumerate(versionList):
        #если  ̶т̶ы̶ ̶п̶и̶д̶о̶р̶  число меньше девяти и это не первый(последний) элемент списка - прибавить к нему один и выйти из цикла
        if number < 9 and index != (len(versionList) - 1):
            versionList[index] += 1
            break
        #если первый(последний) элемент списка - прибавить к нему один
        elif index == (len(versionList) - 1):
            versionList[index] += 1
        #если элемент равен девяти - обнулить его
        else:
            versionList[index] = 0
    
    #перводим список чисел в список строк
    versionList = list(map(str, versionList))
    #переворачиваем для равномерного прогрева шавухи
    versionList = versionList[::-1]
    #объединяем идигриеты в строку
    s = '.'.join(versionList)
    
    return s

# Тесты
try:
    assert next_version("1.2.3") == "1.2.4"
    assert next_version("0.9.9") == "1.0.0"
    assert next_version("1") == "2"
    assert next_version("1.2.3.4.5.6.7.8") == "1.2.3.4.5.6.7.9"
    assert next_version("9.9") == "10.0"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")


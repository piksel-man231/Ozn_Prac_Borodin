# Написать функцию blocks, которая получает строку, состоящую из букв и цифр и возвращает строку в виде блоков,
# разделенных символом дефис. Элементы блока должны быть отсортированы по принципу, указанному ниже, и
# каждый блок не может содержать несколько экземпляров одного и того же символа.
# Порядок блоков:
# строчные буквы (a - z) в алфавитном порядке
# заглавные буквы (A - Z) в алфавитном порядке
# цифры (0 - 9) в порядке возрастания
#
#
# Примеры:
# blocks("21AxBz") ==> "xzAB12"
# blocks("abacad") ==> "abcd-a-a"

import traceback

def blocks(s):
    #чанки для сортировки
    chunks = ['']
    #готовая строка
    sortedStrings = ''
    
    addSymbol = True
    #разбиваем строку на чанки из маленьких букв, больших букв, цифр
    addSymbol = True
    for index, elem in enumerate(s):
        addSymbol = True
        #мелкие буквы
        if not elem.isupper() and not elem.isdigit():
            for indexChunk, elemChunk in enumerate(chunks):
                if not elem in elemChunk and not elemChunk.isupper() and not elemChunk.isdigit():
                    chunks[indexChunk] += elem
                    addSymbol = False
                    break
            if addSymbol:
                chunks.append(elem)
                
                    
        #большие буквы
        if elem.isupper() and not elem.isdigit():
            for indexChunk, elemChunk in enumerate(chunks):
                if not elem in elemChunk and elemChunk.isupper():
                    chunks[indexChunk] += elem
                    addSymbol = False
                    break
            if addSymbol:
                chunks.append(elem)
        #цифры
        if elem.isdigit():
            for indexChunk, elemChunk in enumerate(chunks):
                if not elem in elemChunk and elemChunk.isdigit():
                    chunks[indexChunk] += elem
                    addSymbol = False
                    break
            if addSymbol:
                chunks.append(elem)
    #сортируем чанки
    for i in range(0, len(chunks)):
        chunks[i] = "".join(sorted(chunks[i]))

    #объединяем чанки в строку
    index = 0
    while len(chunks) != 0:
        for i in range(0,len(chunks)):
            if not chunks[i].isupper() and not chunks[i].isdigit():
                sortedStrings += chunks[i]
                chunks.pop(i)
                break
                
        for i in range(0,len(chunks)):
            if chunks[i].isupper() and not chunks[i].isdigit():
                sortedStrings += chunks[i]
                chunks.pop(i)
                break
            
        for i in range(0,len(chunks)):
            if chunks[i].isdigit():
                sortedStrings += chunks[i]
                chunks.pop(i)
                break
        if len(chunks) != 0:
            sortedStrings += "-"
    return sortedStrings

#print(blocks("21AxBz"))


# Тесты
try:
    assert blocks("21AxBz") == "xzAB12"
    assert blocks("abacad") == "abcd-a-a"
    assert blocks("heyitssampletestkk") == "aehiklmpsty-ekst-est"
    assert blocks("6zjX9qcwTIuYNvdmL3CtElHa2n0rogKsSVPRWG4QAMUOe8JkyfxZDiBpb1Fh75GUTLMcbio7HO6rvn1NtDRmPJAejuXVFgaZI3pK90s4fBzqwEd5yWCQh8Sl2kxY") == \
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

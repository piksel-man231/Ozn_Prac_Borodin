"""
Создать txt-файл, вставить туда любую англоязычную статью из Википедии.
Реализовать одну функцию, которая выполняет следующие операции:
- прочитать файл построчно;
- непустые строки добавить в список;
- удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы);
- объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
- создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
  где ключом будет уникальное слово, а значением - количество;
- вывести в порядке убывания 10 наиболее популярных слов, используя метод format
  (вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
- заменить все эти слова в строке на слово “PYTHON”;
- создать новый txt-файл;
- записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
  и не делить слова.
"""
import codecs
import re

def wiki_function():
    wikiText = codecs.open('wiki.txt', 'r', 'utf_8_sig')
    wikiList = []
    
    #непустые строки добавить в список
    for line in wikiText:
      if line and line != '\r\n':
        wikiList.append(line)

    #закрываем файл для не надобности
    wikiText.close()
    
    #удалить из каждой строки все цифры, знаки препинания, скобки, кавычки и т.д. (остаются латинские буквы и пробелы)
    for i in range(0, len(wikiList)):
      #могучие СУКА РЕГУЛЯРКИ. Ебись с их пониманием теперь )))))))))
      wikiList[i] = re.sub(r'[^a-zA-Z\s]+', '', wikiList[i])
      wikiList[i] = (re.sub(r'[\r\n]+', '', wikiList[i])).strip()
      wikiList[i] = re.sub(r' +', ' ', wikiList[i])
    
    #объединить все строки из списка в одну, используя метод join и пробел, как разделитель;
    wikiString = ' '.join(wikiList)

    #создать словарь вида {“слово”: количество, “слово”: количество, … } для подсчета количества разных слов,
    #где ключом будет уникальное слово, а значением - количество;
    wikiDict = {wikiString.split(' ')[0].lower(): 1}
    
    wikiWordsList = wikiString.split(' ')
    
    for word in wikiWordsList:
      addWord = True
      
      for key in wikiDict.copy():
        if word.lower() == key:
          wikiDict[key] += 1
          addWord = False
          break
        
      if addWord:
        wikiDict[word.lower()] = 1
    
    #вывести в порядке убывания 10 наиболее популярных слов, используя метод format
    #(вывод примерно следующего вида: “ 1 place --- sun --- 15 times \n....”);
    wikiListReplace = wikiString.split(' ')
    
    place = 1
    for key, item in sorted(wikiDict.items(),key=lambda item: item[1], reverse=True)[:10]:
      print("{0} place --- {1} --- {2} times \n".format(place, key, item))\
      #заменить все эти слова в строке на слово “PYTHON”;
      for index, elem in enumerate(wikiListReplace):
        if elem == key:
          wikiListReplace[index] = "PYTOHN"
          
      place += 1
    
    wikiString = ' '.join(wikiListReplace)
    
    #записать строку в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов
    #и не делить слова.
    readyTxt = codecs.open('readyTxt.txt', 'w', 'utf_8_sig')
    
    step = 0
    stepEnd = 1
    print(wikiString)
    
    while True:
        stepEnd += wikiString[step: step + 100].rfind(' ')
        if stepEnd == step:
          break
        readyTxt.write(wikiString[step: stepEnd] + "\n")
        print(step, stepEnd, wikiString[step: stepEnd])
        step = stepEnd

    readyTxt.close()

    return 1


# Вызов функции
wiki_function()
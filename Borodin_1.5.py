market = [
            {'id':1, 'product':'Coca-Cola', 'department':'Drinks', 'price':100, 'weight':0.5},
            {'id':2, 'product':'Still_Water', 'department':'Drinks', 'price':30, 'weight':0.5},
            {'id':3, 'product':'Bread', 'department':'Bakery', 'price':25, 'weight':0.3},
            {'id':4, 'product':'Meat', 'department':'Fresh_meat', 'price':250, 'weight':1},
            {'id':5, 'product':'Tomatoes', 'department':'Grossery', 'price':70, 'weight':1},
            {'id':6, 'product':'Cucumbers', 'department':'Grossery', 'price':60, 'weight':1},
            {'id':7, 'product':'Potatoes', 'department':'Grossery', 'price':90, 'weight':1},
            {'id':8, 'product':'Potato_Chips', 'department':'Snacks', 'price':100, 'weight':0.2},
            {'id':9, 'product':'Crackers', 'department':'Snacks', 'price':140, 'weight':0.5},
            {'id':10, 'product':'Milk', 'department':'Grossery', 'price':79, 'weight':0.5}
        ]

def printInfoAllProduct(market):
    for i in market[0]:
        print(f"{i:12} |", end=" ")
    
    print()
    for product in market:
        for j in product:
            print(f"{product[j]:12} |", end=" ")
        print()

def printProductWithId(market):
    id = int(input("Введите id товара - "))
    idFind = False
    
    for product in market:
        if id == product["id"]:
            idFind = True
            for j in product:
                print(f"{j} : {product[j]} |", end=" ")
        print()  

    if not idFind:
        print("товара с таким id не существует, пёс")

def printDepartmentCount(market):
    department = input("Введите название отдела - ")
    count = 0
    
    for product in market:
        if department == product["department"]:
            count += 1
            
    if count == 0:
        print("Такого отдела не существет")
    else:
        print(f"Количество товаров в отделе {department} - {count}")

def changeProductWithId(market):
    id = int(input("Введите ид товара, которого хотите поменять - "))
    
    for product in market:
        if id == product["id"]:
            for j in product:
                product[j] = input(f"Введите значение для {j} - ")

def delProductWithId(market):
    id = int(input("Введите ид товара, которогы хотите удалить - "))
    
    for product in market:
        if id == product["id"]:
            market.remove(product)
    
print('''
    1 – вывод информации о всех товарах; \n
    2 – вывод информации о товаре по введенному с клавиатуры номеру; \n
    3 – вывод количества товаров, продающихся в определнном отделе; \n
    4 – обновлении всей информации о товаре по введенному номеру; \n
    5 – удалении товара по номеру; \n
    0 - выход из программы.
    ''')

while True:
    whatMeDo = int(input("Выберите функцию - "))

    if whatMeDo == 1:
        printInfoAllProduct(market)
    elif whatMeDo == 2:
        printProductWithId(market)
    elif whatMeDo == 3:
        printDepartmentCount(market)
    elif whatMeDo == 4:
        changeProductWithId(market)
    elif whatMeDo == 5:
        delProductWithId(market)
    elif whatMeDo == 0:
        exit()
    
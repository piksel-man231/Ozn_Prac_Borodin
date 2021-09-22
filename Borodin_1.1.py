import traceback


def special_number(number):
    num_string = str(number)
    z = 1
    sum = 0
    for i in num_string:
        sum = sum + pow(int(i), z)
        z = z + 1
    if sum == number:
        return True
    else:
        return False


# Тесты
try:
    assert special_number(1) == True
    assert special_number(2) == True
    assert special_number(89) == True
    assert special_number(77) == False
    assert special_number(518) ==  True
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
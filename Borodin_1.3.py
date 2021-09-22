import traceback


def riders(stations):
    Horse_stamina = 100
    k = 1
    while len(stations)!=0:
        if (Horse_stamina - stations[0]) > 0:
            Horse_stamina -= stations.pop(0)
        else:
            k=k+1
            Horse_stamina = 100
    return k


# Тесты
try:
    assert riders([18, 15]) == 1
    assert riders([43, 23, 40, 13]) == 2
    assert riders([33, 8, 16, 47, 30, 30, 46]) == 3
    assert riders([6, 24, 6, 8, 28, 8, 23, 47, 17, 29, 37, 18, 40, 49]) == 4
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

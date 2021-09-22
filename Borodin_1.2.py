import traceback


def min_sum(arr):
    arr.sort()
    sum = 0
    print (arr)
    while len(arr) != 0:
        sum += arr.pop(0) * arr.pop()
        print (sum)
    return sum


try:
    assert min_sum([5,4,2,3]) == 22
    assert min_sum([12,6,10,26,3,24]) == 342
    assert min_sum([9,2,8,7,5,4,0,6]) == 74
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")

import traceback


def case_sensitive(s):
    upperCase = []
    
    for i in s:
        if i.isupper():
            upperCase.append(i)

    return [ not len(upperCase) > 0, upperCase]

# Тесты
try:
    assert case_sensitive('asd'), [True, []]
    assert case_sensitive('cellS'), [False, ['S']]
    assert case_sensitive('z'), [True, []]
    assert case_sensitive(''), [True, []]
    assert case_sensitive('aaTRggjS'), [True, ['T', 'R', 'S']]
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
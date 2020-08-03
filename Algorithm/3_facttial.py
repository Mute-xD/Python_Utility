"""
尾递归
"""


def factorial(inti, answer=1):
    if inti == 1:
        return answer

    elif inti < 0 or type(inti) is "<class 'int'>":
        raise TypeError('inti unexpected')
    else:
        return factorial(inti - 1, answer * inti)


print(factorial(4))

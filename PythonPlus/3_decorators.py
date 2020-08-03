import time
from functools import wraps

isDebugMode = True
isFuncWork = True


def debugMode(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if isDebugMode:
            start = time.perf_counter_ns()
            func(*args, **kwargs)
            end = time.perf_counter_ns()
            print('Time Count', end - start)

        else:
            func(*args, **kwargs)
    return wrapper  # 注意：wrapper后会自动补全括号，注意删掉


def functionSwitch(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if isFuncWork:
            func(*args, **kwargs)
        else:
            # print('NOT WORK')
            pass
    return wrapper


@functionSwitch
@debugMode
def helloWorld(int1):
    print('Hello World')
    print(int1)


helloWorld(123)

from functools import wraps
import time


def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'Calling {func.__name__} with {args} {kwargs}')
        return func(*args, **kwargs)

    return wrapper
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        print('Time:', time.time() - t0)
        return result
    return wrapper


@timer
@logger
def process(x):
    time.sleep(1)
    return x * 2


process(5)

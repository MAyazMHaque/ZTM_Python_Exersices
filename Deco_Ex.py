## Creating own decorator to find out how long other function takes
from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
           t1 = time()
           result = fn(*args, **kwargs)
           t2 = time()
           print(f'took ime {t2-t1} seconds')
           return result
    return wrapper


@performance
def log_time(n):
    for i in range(n):
        i * 5

log_time(1000000000)

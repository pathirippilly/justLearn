from functools import wraps
from time import time
def speed_test(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print(args)
        print(kwargs)
        start_time=time()
        result=func(*args,**kwargs)
        end_time=time()
        print(f"executing {func.__name__}")
        print(f"Time Elapsed {end_time-start_time}")
        return result
    return wrapper
@speed_test
def sum_nums_gen(num):
    return sum(x for x in range(num))
@speed_test
def sum_nums_list(num):
    return sum([x for x in range(num)])       

print(sum_nums_list(100000))
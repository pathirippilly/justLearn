from functools import wraps

import time
import os
def dec_func(func):
    def wrap_func(*args):
        print(f"execution of the function {func.__name__} has started..")
        print(func(*args))
        print("execution of the function has ended..")
    return wrap_func
class dec_class():
    def __init__(self,orig_func):
        self.orig_func=orig_func
    def __call__(self,*args):
        print(f"executing {self.orig_func.__name__}")
        return self.orig_func(*args)

@dec_func
#@dec_class
def add(a,b):
    return a + b

#add(5,6)

##Logger and Timer implementations using decorators
#######################################################

def my_logger(func):
    logging.basicConfig(filename=f'{func.__name__}.log',level=logging.INFO)

    @wraps(func)
    def wrapper(*args,**kwargs):
        logging.info(f"{func.__name__} ran with args {args} and kwargs {kwargs}")
        return func(*args,**kwargs)
    return wrapper

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t1=time.time()
        result=func(*args, **kwargs)
        t2=time.time()
        print(f"excution time of {func.__name__} is {t2-t1}")
        return result
    return wrapper

@my_logger
@timer
def add(a,b):
    time.sleep(1)
    return a + b
print(add(1,2))

os.path.exists("")
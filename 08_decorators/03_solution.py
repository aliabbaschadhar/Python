import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache 
def long_running_func(n,m):
    time.sleep(2)
    return n+m

print(long_running_func(3,8))
print(long_running_func(3,8))
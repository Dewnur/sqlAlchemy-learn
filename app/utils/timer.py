from timeit import default_timer as timer


def func_timer(func):
    async def wrapper(*args, **kwargs):
        start_time = timer()
        result = await func(*args, **kwargs)
        end_time = timer()
        print(f"{func.__name__} executed in {end_time - start_time} seconds")
        return result

    return wrapper

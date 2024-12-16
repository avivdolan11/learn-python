import functools

def be_nice(fn):
    @functools.wraps(fn)
    def inner(*args, **kwargs):
        print("Nice to meet you")
        result = fn(*args, **kwargs)
        print(result)
        print("It was my pleasure")
        return result
    
    return inner

@be_nice
def complex_business_sum(a, b):
    "Adds two numbers together"
    return a + b

help(complex_business_sum)
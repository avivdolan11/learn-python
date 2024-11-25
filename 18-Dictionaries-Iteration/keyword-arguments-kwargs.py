def length(word):
    return len(word)


print(length("Hello"))
print(length(word = "Hello"))

def collect_keyword_arguments(**kwargs):
    print(kwargs)

    for key, value in kwargs.items():
        print(f"the key is {key} and the value is {value}")

collect_keyword_arguments(a=2, b=4, c=9)

def args_and_kwargs(a, b, *args, **kwargs):
    print(f"the total of regular args a and b is {a+b}")
    print(f"the total of args tuple is {sum(args)}")
    
    dict_total = 0
    for value in kwargs.values():
        dict_total += value
    

    print(f"{dict_total}")



args_and_kwargs(1,2,3,4,5,6, x=10, z=5, y=8)


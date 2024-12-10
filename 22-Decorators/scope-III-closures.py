def outer():
    candy = "snickers"

    def inner():
        return candy
    
    return inner

the_func = outer()
print(the_func())
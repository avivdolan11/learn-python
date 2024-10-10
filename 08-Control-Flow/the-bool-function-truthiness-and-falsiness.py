if 10 > 3:
    print("Hello")


## 0 is falsey value any other number is truthey

if 3:
    print("Hey")    


print(bool(1))
print(bool(0))



def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    if number % 2 != 0:
        return "odd" 
    

def truthy_or_falsy(arg):
    if bool(arg):
     return f"The value {arg} is truthy"

    return f"The value {arg} is falsy"
      
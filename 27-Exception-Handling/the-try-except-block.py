def divide_five_by_num(n):
    try:
        calculation = 5/n
    except:
        calculation = 5

    return calculation

print(divide_five_by_num(0))
print(divide_five_by_num(10))
print(divide_five_by_num("HEY"))
def divide_five_by_num(n):
    try:
        calculation = 5/n
    except ZeroDivisionError:
        return "You cant divide by zero"
    except TypeError as e:
        return f"No dividing by invalid objects. {e}"

    return calculation

print(divide_five_by_num(0))
print(divide_five_by_num(10))
print(divide_five_by_num("HEY"))
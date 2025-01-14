def add_pos_num(a, b):
    try:
        if a <= 0 or b <= 0:
            raise ValueError("One or both values is invalid")
    
        return a + b
    
    except ValueError as e:
        return f"Caught the value error. {e}"
    
print(add_pos_num(10,5))
print(add_pos_num(-10,5))
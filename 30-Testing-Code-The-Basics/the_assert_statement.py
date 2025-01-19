def add(a, b):
    assert isinstance(a, int) and isinstance(b, int), "Both arguments must be integers"
    return a + b

print(add(3,8))
print(add(3,"8"))
import copy

# a = [1,2,3]

# b = a[:]

# print(a == b)
# print(a is b)

# c = a.copy()

# d = copy.copy(a)

numbers = [2,3,4]
a = [1, numbers, 5]

b = a[:]
b = a.copy()
b = copy.copy(a)
b = copy.deepcopy(a)

print(a[1] is b[1])
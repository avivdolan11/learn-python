print(type({"a": 2}))

print(isinstance(1, int))
print(isinstance({"a":2}, dict))
print(isinstance([], list))
print(isinstance([], float))

print(isinstance(1, object))
print(isinstance([], (list, dict)))
print(isinstance([], (int, dict)))

class Person():
    pass

class SuperHero(Person):
    pass

arnold = Person()
boris = SuperHero()

print(isinstance(arnold, SuperHero))
print(isinstance(boris, SuperHero))
print(isinstance(boris, Person))


print(issubclass(SuperHero, Person))
print(issubclass(Person, SuperHero))
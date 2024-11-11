def accept_stuff(*args):
    print(type(args))
    print(args)

accept_stuff(1)
accept_stuff(1,3,5)
accept_stuff(1,3,5,32,4,6)
accept_stuff()


def my_max(nonsense, *args):
    print(nonsense)
    greatest = args[0]
    for arg in args:
        if arg > greatest:
            greatest = arg
    
    return greatest

print(my_max("Hello",4,6,889,3,232,1000,2,2,4))
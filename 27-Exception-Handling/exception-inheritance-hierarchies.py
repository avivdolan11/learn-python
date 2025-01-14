class Mistake(Exception):
    pass

class StupidMistake(Mistake):
    pass

class SillyMistake(Mistake):
    pass

try:
    raise StupidMistake("Extra Stupid")
except StupidMistake as e:
    print(f"Caught the error: {e}")

try:
    raise StupidMistake("Extra Stupid")
except SillyMistake as e:
    print(f"Caught the error: {e}")
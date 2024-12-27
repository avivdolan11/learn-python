class Counter():
    count = 0

    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def create_two(cls):
        two_counters = [cls(), cls()]
        return two_counters

print(Counter.count)
c1 = Counter()
print(Counter.count)

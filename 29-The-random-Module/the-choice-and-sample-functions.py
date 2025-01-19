import random 

print(random.choice(["Bob", "Moe", "Curly"]))
print(random.choice((1,2,3)))

lottery_numbers = [random.randint(1,50) for number in range(50)]
print(lottery_numbers)

print(random.sample(lottery_numbers, 5))
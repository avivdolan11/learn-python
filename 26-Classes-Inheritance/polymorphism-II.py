import random

class Player():
    def __init__(self, games_played, victories):
        self.games_played = games_played
        self.victories = victories

    @property
    def win_ratio(self):
        return self.victories / self.games_played
    

class Human(Player):
    def make_move(self):
        print("Let player make decision")

class Computer(Player):
    def make_move(self):
        print("Run algorithm to make best move")


hp = Human(30, 15)
comp = Computer(1000, 999)

print(hp.win_ratio)
print(comp.win_ratio)

game_players = [hp, comp]
starting = random.choice(game_players)

starting.make_move()

## Exercise 
import random

class DentalHealthItem():
    def __init__(self, price):
        self.price = price
        

class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"
        
class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"
        
class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"
        

toothbrush = Toothbrush(2.99)
floss = Floss(1.99)
mouthwash = Mouthwash(5.99)

dental_health_kit = [toothbrush, floss, mouthwash]

random.shuffle(dental_health_kit)

actions = [item.use() for item in dental_health_kit]

print(actions)
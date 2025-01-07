class Emotion():
    def __init__(self, positivity, negativity):
        self.positivity = positivity
        self.negativity = negativity
    
    def __bool__(self):
        return self.positivity > self.negativity
    

state_emotional = Emotion(50,75)
print(state_emotional)
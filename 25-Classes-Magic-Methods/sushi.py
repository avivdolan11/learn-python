"""
A module related to sushi no fishy code here
"""

def fish():
    """
    Determines if fish is a good meal choice
    """
    return True


class Salmon():
    """
    Blueprint for salmon object
    """
    def __init__(self):
        self.tastiness = 10
    
    def bake(self):
        """
        Bake the fish in the oven
        """
        self.tastiness += 1
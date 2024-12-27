class Guitar():
    def __init__(self, wood):
        self.wood = wood

acoustic = Guitar("Alder")
electric = Guitar("Mahogany")

print(acoustic.wood)
print(electric.wood)


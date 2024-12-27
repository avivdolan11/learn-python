class Currency():
    def __init__(self, dollars):
        self._cents = dollars * 100

    @property
    def dollars(self):
        return self._cents / 100
    
    @dollars.setter
    def dollars(self, dollars):
        if dollars >= 0:
            self._cents = dollars * 100
    

bank_account = Currency(50000)
print(bank_account.dollars)

bank_account.dollars = 100000
print(bank_account.dollars)

bank_account.dollars = -200000
print(bank_account.dollars)


class PizzaPie():
    def __init__(self, total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0
    
    @property
    def slices_eaten(self):
        return self._slices_eaten
    
    @slices_eaten.setter
    def slices_eaten(self, slices_eaten):
        if slices_eaten <= self.total_slices:
            self._slices_eaten = slices_eaten
    
    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices


pp = PizzaPie(8)
print(pp.slices_eaten)

pp.slices_eaten = 100
print(pp.slices_eaten)
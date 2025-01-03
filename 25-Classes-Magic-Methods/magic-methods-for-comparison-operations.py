class Student():
    def __init__(self, math, history, writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing
    
    def __eq__(self, other_student):
        return self.grades == other_student.grades
    
    def __gt__(self, other_student):
        return self.grades > other_student.grades
    
    def __le__(self, other_student):
        return self.grades <= other_student.grades
    
    def __add__(self, other_student):
        return self.grades + other_student.grades
    
    def __sub__(self, other_student):
        return self.grades - other_student.grades

bob = Student(90, 90, 90)
moe = Student(100, 90, 80)
jo = Student(40, 45, 50)

print(moe > jo)
print(bob + moe)




### Equality and String Representation

class BusTrip():
    def __init__(self, destination, company, price):
        self.destination = destination
        self.company = company
        self.price = price

    def __repr__(self):
        return f'You paid {self.price} to {self.company} to go to {self.destination}.'
    
    def __eq__(self, other_trip):
        same_destination = self.destination == other_trip.destination
        insignificant_price_diff = abs(self.price - other_trip.price) <= 3
        return same_destination and insignificant_price_diff
    


boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
print(boston1)
print(boston1 == boston2)
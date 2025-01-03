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

bob = Student(90, 90, 90)
moe = Student(100, 90, 80)
jo = Student(40, 45, 50)

print(bob.grades)
print(moe.grades)
print(jo.grades)

print(bob == moe)
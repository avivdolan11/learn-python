class Employee():
    def do_work(self):
        print("Im working")

class Manager(Employee):
    def waste_time(self):
        print("Wow im distracted")

class Director(Manager):
    def fire_employee(self):
        print("Youre fired")

e = Employee()
m = Manager()
d = Director()

e.do_work()
m.waste_time()
m.do_work()

d.do_work()
d.fire_employee()
d.waste_time()
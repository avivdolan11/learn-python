class Teacher():
    def teach_class(self):
        print("Teaching stuff")

    def grab_lunch(self):
        print("Yum Yum")

    def grade_tests(self):
        print("F, F, F")


class CollegeProfessor(Teacher):
    def publish_books(self):
        print("Hooray im an author")

    def grade_tests(self):
        print("A, A, A")


teacher = Teacher()
professor = CollegeProfessor()

teacher.grab_lunch()
teacher.grade_tests()
teacher.teach_class()

professor.publish_books()
professor.grab_lunch()
professor.teach_class()
professor.grade_tests()


### Exercise 
class Clothing():
    def wear(self):
        return "I'm wearing this fashionable piece of clothing!"
    
    def sell(self):
        return "Buy my piece of clothing!"

class Socks(Clothing):
    def lose_one(self):
        return "Where did my other one go?"
        
    def wear(self):
        return "Take a look at my socks! They're gorgeous!"
        
    def sell(self):
        return "Buy my socks!"
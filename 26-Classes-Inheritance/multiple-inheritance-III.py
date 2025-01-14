class FilmMaker():
    def give_interview(self):
        print("I love making movies")

class Director(FilmMaker):
    pass

class ScreenWriter(FilmMaker):
    def give_interview(self):
        print("I love writing scripts")


class JackOfAllTrades(Director, ScreenWriter):
    pass

jack = JackOfAllTrades()

jack.give_interview()

print(JackOfAllTrades.mro())
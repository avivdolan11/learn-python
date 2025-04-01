class WeatherForecast():
    def __init__(self, temperatures):
        self.temperatures = temperatures

    @staticmethod
    def convert_from_far_to_cels(fahr):
        calculation = ((5/9) * (fahr - 32))
        return round(calculation, 1)

    def in_celsius(self):
        return [self.convert_from_far_to_cels(temp) for temp in self.temperatures]

wf = WeatherForecast([100,90,80,70,60])
print(wf.in_celsius())
#import datetime
from datetime import date

birthday = date(2000, 9, 11)
print(birthday)
print(type(birthday))

moon_landing = date(year = 1969, month = 7, day = 20)
print(moon_landing)


print(birthday.month)
print(birthday.year)

today = date.today()

print(today)
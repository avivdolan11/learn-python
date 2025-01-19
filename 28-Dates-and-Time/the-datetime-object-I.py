from datetime import datetime

print(datetime(1999, 7, 24))
print(datetime(1999, 7, 24, 14, 30))
print(datetime(1999, 7, 24, 14, 30, 55))
print(datetime(year=1999, month=7, day=24, hour=14, minute= 30, second=55))

today = datetime.today()
print(today)
print(datetime.now())

print(today.weekday())

same_time_20_years_ago = today.replace(year= 2005)
print(same_time_20_years_ago)
from datetime import datetime, timedelta

birthday = datetime(2000, 9, 11)
today = datetime.now()

lifespan = today - birthday
print(lifespan)
print(type(lifespan))

print(lifespan.total_seconds())

five_hundred_days = timedelta(days = 500, hours = 12)
print(five_hundred_days)

print(five_hundred_days + five_hundred_days)

print(today + five_hundred_days)
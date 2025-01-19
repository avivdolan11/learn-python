from datetime import datetime

today= datetime.today()

print(today.strftime("%m"))
print(today.strftime("%d"))
print(today.strftime("%m %d"))
print(today.strftime("%m/%d/%Y"))

print(today.strftime("%A"))
print(today.strftime("%B"))
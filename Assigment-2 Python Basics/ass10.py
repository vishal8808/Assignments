from datetime import datetime
dt = datetime.today();
print(dt)
d1=dt.strftime("%d-%m-%Y and %I:%M %p")
print(d1)
d1=dt.strftime("%d-%m-%y")
print(d1)

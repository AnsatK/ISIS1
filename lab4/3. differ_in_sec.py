import datetime

time1 = datetime.datetime.now()
time2 = datetime.datetime.now()+datetime.timedelta(seconds=343242)
print((time2-time1).total_seconds())


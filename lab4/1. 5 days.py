import datetime

today = datetime.date.today()
fivedaysago= today - datetime.timedelta(5)
print(fivedaysago)
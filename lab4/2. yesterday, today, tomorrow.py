import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(1)
tommorow = today + datetime.timedelta(1)
print("Yesterday: " + str(yesterday))  
print("Today: " + str(today)) 
print("Tommorow: " + str(tommorow))
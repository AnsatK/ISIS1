import datetime

now = datetime.datetime.now()
now_without_ms = now.replace(microsecond = 0)
print(now)
print(now_without_ms)
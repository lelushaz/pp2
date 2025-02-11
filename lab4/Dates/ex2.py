import datetime
today= datetime.datetime.now()
tomorrow=today+datetime.timedelta(days=1)
yesterday=today-datetime.timedelta(days=1)
print(today.strftime("%x"))
print(tomorrow.strftime("%x"))
print(yesterday.strftime("%x"))
import datetime

now =datetime.datetime.now()
print(now)
print(now.day)
print(now.month)
print(now.minute)
print(now.second)
print(now)
now=now.replace(minute=0)
before=now.replace(minute=0, second=0,microsecond=0)
print(before)
#after=before + datetime.timedelta(days=5,minutes=30,hours=5)
#print(after)
time_elapsed= datetime.datetime.now() - now
minute = time_elapsed.seconds / 60
minute =round(minute)
print(time_elapsed)
print(time_elapsed.days)
print(minute)
print(time_elapsed.seconds)
print(time_elapsed.microseconds)

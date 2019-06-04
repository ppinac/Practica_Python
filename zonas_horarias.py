import datetime
central_time = datetime.timezone(datetime.timedelta(hours = -6))
pacific_time =datetime.timezone(datetime.timedelta(hours = -8))
eastern_time =datetime.timezone(datetime.timedelta(hours = -5))

now = datetime.datetime.now(central_time)
now =now.astimezone(pacific_time)
print(now)
now =now.astimezone(eastern_time)
print(now)


#print(central_time)
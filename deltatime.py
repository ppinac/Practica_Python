import datetime

now =datetime.datetime.now()
print(now)
before =now + datetime.timedelta(days =5)
after = before +datetime.timedelta(days=5,minutes=30,hours=5)
print(before)
print(after)
print ("dias \n" + str(now.date()))
print(before.date())
print(after.date())

print("Tiempo \n"+ str(now.time()))
print(before.time())
print(after.time())

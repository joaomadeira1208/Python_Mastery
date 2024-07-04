from datetime import datetime
import time

dt = datetime(2018, 1, 1)
dt_2 = datetime.now()
dt_3 = datetime.strptime("2018/01/02", "%Y/%m/%d")

dt_4 = datetime.fromtimestamp(time.time())

print(dt)
print(dt_2)
print(dt_3)
print(dt_4)

print("----------------------")

print(f"{dt.year}/{dt.month}")
print(dt.strftime("%Y/%m"))

print("----------------------")

print(dt_2 > dt)

from datetime import datetime, timedelta

dt1 = datetime(2018, 1, 1)
dt2 = datetime.now()

duration = dt2 - dt1

print(duration)  # Type : class 'datetime.timedelta'
print("days", duration.days)
print("seconds", duration.seconds)
print("seconds", duration.total_seconds())  # Total duration in seconds

dt1 = dt1 + timedelta(days=1, seconds=1000)

print(dt1)

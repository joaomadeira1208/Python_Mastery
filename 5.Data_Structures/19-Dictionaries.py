point = {"x": 1, "y": 2}
point = dict(x=1, y=2)  # This is the same as the previous line

point["x"] = 10
point["z"] = 20
print(point)

if "a" in point:
    print(point["a"])


print(point.get("a"))
print(point.get("a", 0))
del point["x"]
print(point)


for key in point:
    print(key, point[key])

for key, value in point.items():
    print(key, value)

import json
from pathlib import Path

# movies = [
#     {"id": 1, "title": "The Shawshank Redemption", "year": 1994},
#     {"id": 2, "title": "The Godfather", "year": 1972},
#     {"id": 3, "title": "The Dark Knight", "year": 2008}
# ]

# # CONVERT PYTHON OBJECT TO JSON
# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)


# READ JSON FILE

data = Path("movies.json").read_text()

movies = json.loads(data)
print(movies)
print("-----------------")
print(movies[0])
print(movies[0]["title"])

import json
from pathlib import Path
from random import shuffle

# data = []
#
# pathlist = Path("../data/cleaned data").rglob("*.json")
# for path in pathlist:
#     path_in_str = str(path)
#
#     with open(path_in_str, encoding="utf-8") as file:
#         raw = json.load(file, strict=False)
#         data += raw
#
# shuffle(data)
#
# with open("../data/all-tweets.json", "w+", encoding="utf-8") as out:
#     json.dump(data, out)


# with open("../data/all-tweets.json", encoding="utf-8") as data:
#     data = json.load(data)
#
# print(len(data))

data = []

pathlist = Path("../data/cleaned data").rglob("*.json")
for path in pathlist:
    path_in_str = str(path)

    with open(path_in_str, encoding="utf-8") as file:
        raw = json.load(file, strict=False)
        raw = raw[0:250]
        data += raw

shuffle(data)

with open("../data/training data/training raw.json", "w+") as file:
    json.dump(data, file)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import json
import datetime


# change these \/ \/ \/ ---------------

tag = "#hydroxychloroquine"
target = "hydroxychloroquine"
raw = "data/cleaned data/hydroxychloroquine + 2020-01 - 2020-10-31.json"

# -------------------------------------

colors = {
    "covidhoax": "green",
    "hydroxychloroquine": "lightblue",
    "antimask": "red",
    "microchip": "purple"
}

inPro = "../data/training data/{}/pro-conspiracy.txt".format(target)
inAnti = "../data/training data/{}/anti-conspiracy.txt".format(target)
inNeutral = "../data/training data/{}/conspiracy-neutral.txt".format(target)

rawData = "../{}".format(raw)


with open(rawData) as file:
    data = json.load(file, strict=False)

# density = {}
#
# for d in data:
#     if d["date"] not in density:
#         density[d["date"]] = 1
#     else:
#         density[d["date"]] += 1
#
# mpl_data = [(k, v) for k, v in density.items()]
#
# print(density)
# for t in density.keys():
#     print(mdates.datestr2num(t))

mpl_data = [mdates.datestr2num(i["date"]) for i in data]

fig, ax = plt.subplots(1, 1)
ax.hist(mpl_data, bins=283, color=colors[target])

ax.set_title(tag)
ax.set_ylabel("Tweets per day")
ax.set_xlabel("Time")

fig.set_size_inches(15, 7)

ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m.%y"))

ax.set_xlim([
    datetime.date(2020, 1, 1),
    datetime.date(2020, 10, 31)
])

plt.show()

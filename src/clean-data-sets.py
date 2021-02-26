import json


files = ["covidhoax + 2020-01-01 - 2020-05-19.json", "covidhoax + 2020-05-19 - 2020-10-31.json"]

target = "covidhoax + 2020-01-01 - 2020-10-31.json"

data = []

for file in files:

    print("Currently processing {}...".format(file))

    file = "../data/raw data/" + file

    num_lines = sum(1 for line in open(file, encoding="utf-8"))

    with open(file, encoding="utf-8") as opened:
        for count, line in enumerate(opened):

            print("{}% complete".format(100 * count / num_lines))

            rawData = json.loads(line.strip())

            if rawData["language"] != "en":
                continue

            if not any(rawData["id"] == existingId for existingId in data):
                data.append({
                    "id": rawData["id"],
                    "date": rawData["date"],
                    "time": rawData["time"],
                    "timezone": rawData["timezone"],
                    "language": rawData["language"],
                    "tweet": rawData["tweet"]
                })

cleanedData = json.dumps(data)
cleanedData = cleanedData.replace("},", "},\n")

with open("../data/cleaned data/" + target, "w+") as outfile:
    outfile.write(cleanedData)

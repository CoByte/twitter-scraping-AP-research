from pathlib import Path
import json


def strip_lang(item):
    item.pop("language", None)
    return item


def remove_unicode(item):
    text = item["tweet"]
    text = text.encode("ascii", "ignore")
    text = text.decode()
    item["tweet"] = text
    return item


pathlist = Path("../data/cleaned data").rglob("*.json")
for path in pathlist:
    path_in_str = str(path)

    print(path_in_str)

    with open(path_in_str) as file:
        data = json.load(file, strict=False)

    # data = list(map(strip_lang, data))
    data = list(map(remove_unicode, data))

    cleanedData = json.dumps(data)
    cleanedData = cleanedData.replace("},", "},\n")

    with open(path_in_str, "w") as outfile:
        outfile.write(cleanedData)

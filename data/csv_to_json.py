import csv
import json


def converter(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_file:
        for row in csv.DictReader(csv_file):
            record = {"model": model, "pk": row["Id"]}
            del row["Id"]

            if "price" in row:
                row["price"] = int(row["price"])

            if "is_published" in row:
                if row["is_published"] == 'True':
                    row["is_published"] = True
                else:
                    row["is_published"] = False

            record["fields"] = row
            result.append(record)

    with open(json_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(result, ensure_ascii=False))


converter('categories.csv', 'categories.json', 'ads.categories')
converter('ads.csv', 'ads.json', 'ads.ads')

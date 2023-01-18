import csv
import json


def converter(csv_file, json_file, model):
    result = []
    with open(csv_file, encoding='utf-8') as csv_file:
        for row in csv.DictReader(csv_file):
            record = {"model": model, "pk": row["id"]}
            del row["id"]

            if "price" in row:
                row["price"] = int(row["price"])

            if "is_published" in row:
                if row["is_published"] == 'TRUE':
                    row["is_published"] = True
                else:
                    row["is_published"] = False
            if "location_id" in row:
                row['location'] = [row["location_id"]]
                del row['location_id']


            record["fields"] = row
            result.append(record)

    with open(json_file, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(result, ensure_ascii=False))


converter('datasets/ad.csv', 'ads.json', 'ads.ad')
# converter('datasets/category.csv', 'category.json', 'ads.category')
# converter('datasets/location.csv', 'location.json', 'users.location')
# converter('datasets/user.csv', 'user.json', 'users.user')

import csv

with open('sample.csv', 'r', encoding="utf-8", newline='')as fp:
    csv_reader = csv.reader(fp)
    # 跳過標題欄
    next(csv_reader)

    for row in csv_reader:
        print(row[0])


with open('sample.csv', 'r', encoding="utf-8", newline='')as fp:
    csv_reader = csv.DictReader(fp)

    for row in csv_reader:
        print(row['區名'])

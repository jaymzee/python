import csv

with open('food.csv', 'r') as f:
    csv_reader = csv.DictReader(f)

    for row in csv_reader:
        print("'%s' '%s'" % (row['name'], row['favorite food']))

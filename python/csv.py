import csv

# create new csv
file = open('temporary.csv', 'r+')
# read from csv
reader = csv.reader(csv_file)

# skip header
header = next(reader)

# build whole file from memory
csv_file = build_csv(parsed, header=['ip', 'time_local', 'request_type'], file=file)

# read into a list
apps_data = list(reader)
# read all lines
csv_file.readlines()
# iteration
for line in reader:


writer = csv.writer(file, delimiter=',')
writer.writerows(lines)


file.seek(0)






def count_unique_request(csv_file):
    reader = csv.reader(csv_file)
    header = next(reader)
    idx = header.index('request_type')
    
    uniques = {}
    for line in reader:
        
        if not uniques.get(line[idx]):
            uniques[line[idx]] = 0
        uniques[line[idx]] += 1
    return uniques


# generator functions
# closures
# use functions as decorators
# instance methods
import csv
import os
import glob
import os

root_dir = '.'
for directory, subdirectories, files in os.walk(root_dir):
    for file in files:
        print(os.path.join(directory, file))
#some debug prints
for filepath in glob.iglob('my_dir/*.csv'):
    print(filepath)

for file in os.listdir(directory):
    if file.endswith(".csv"):
        with open(os.path.join(file), 'r') as read_object, open(file+'data_output.csv', 'w') as write_object:
            csv_reader = csv.reader(read_object)
            csv_writer = csv.writer(write_object, lineterminator='\n')
            data = csv.DictReader(read_object)
            list = []
            row = next(csv_reader)
            row.append('Change')
            list.append(row)
            for row in csv_reader:
                row.append((float(row[4]) - float(row[1])) / float(row[1]))
                list.append(row)
            csv_writer.writerows(list)

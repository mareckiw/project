import os
import csv
from csv import writer,reader
from urllib.request import urlopen

url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1587042293&period2=1618578293&interval=1d&events=history&includeAdjustedClose=true'
url2 = 'https://query1.finance.yahoo.com/v7/finance/download/IBM?period1=1587157611&period2=1618693611&interval=1d&events=history&includeAdjustedClose=true'
url3 = 'https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=1587157804&period2=1618693804&interval=1d&events=history&includeAdjustedClose=true'
#local_path = os.path.join('data', 'GOOG.csv')
with urlopen(url) as image, open('GOOG.csv', 'wb') as f:
    f.write(image.read())
with urlopen(url2) as image, open('IBM.csv', 'wb') as f:
    f.write(image.read())
with urlopen(url3) as image, open('MSFT.csv', 'wb') as f:
    f.write(image.read())

# with open('GOOG.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     rows = list(csv_reader)
#     print(rows[1])
#     import csv
new_col = []
# with open('GOOG.csv','r', newline='') as csvfile:
#     data = csv.DictReader(csvfile)
#
#     fieldnames = ['Change'] + data.fieldnames # add column name to beginning
#     #csvwriter = csv.DictWriter(csvout, fieldnames)
#     header = next(data)
#     print("Close | Open | Change")
#     print("---------------------------------")
#
#     for row in data:
#         change = row['Change'] = (float(row['Close'])-float(row['Open']))/float(row['Open'])
#         print(row['Close'],'|', row['Open'], '|',change)
#         print(type(change),change)
#         #new_col.append(change)
#     with open('GOOG2.csv', 'w', newline='') as csvout:
#         csv_reader = reader(csvfile)
#     csv_writer = writer(csvout)
#     for row in csv_reader:
#         row.append(str(change))
#         csv_writer.writerow(row)
#        # csvwriter.writerow(dict(row, Change='change %s' % list))
#     #print(new_col)
# list = [['Geeks for Geeks', '2008', 'Sandeep Jain'],
#          ['HackerRank', '2009', 'Vivek Ravisankar']]
# with open('GOOG.csv', 'a+', newline ='') as file:
#     write = csv.writer(file)
#     write.writerows(data)

# with open('GOOG.csv', 'a') as csvout:
#     writefile = csv.writer(csvout, delimiter=',', lineterminator='\n')
#     for row in writefile:
#         writefile.writerow(int(change))

# with open('GOOG.csv', mode='w') as stocks_file:
#     employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#
#     employee_writer.writerow(['John Smith', 'Accounting', 'November'])
#     employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
# with open('IBM.csv', 'w', ) as file:
#     stocks = csv.reader(file, delimiter=' ', quotechar='|')
#     for row in stocks:
#         print(', '.join(row))

# print('------ JSON -------')
# import json
# out_file = 'out_list.json'
# with open(out_file, 'w') as f:
#     json.dump(l1, f)
yourList = [4,5,6]

# with open('GOOG.csv', 'w', ) as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     for word in yourList:
#         wr.writerow([word])



with open('GOOG.csv', 'r') as read_object, open('data_output.csv', 'w') as write_object:
    csv_reader = csv.reader(read_object)
    csv_writer = csv.writer(write_object, lineterminator='\n')
    data = csv.DictReader(read_object)
    # for row in data:
    #     change = str((float(row['Close'])-float(row['Open']))/float(row['Open']))
    #     print(type(change),'change:', change)
    list = []
    row = next(csv_reader)
    row.append('Change')
    list.append(row)
    for row in csv_reader:
        row.append((float(row[4]) - float(row[1])) / float(row[1]))
        list.append(row)
        #change2 = row[5]
        #change3 = row[2]
        #change4 = change2-change3
        #print(change3)
        #new_column_text = str(change3)
        #row.append(new_column_text)
    csv_writer.writerows(list)
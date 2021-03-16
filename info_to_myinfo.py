import csv
import re

employee_file = open('my_info.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# employee_writer.writerow(['John Smith', 'Accounting', 'November'])
# employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open("info.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        # print ('line[{}] = {}'.format(i, line))
        print(line[0])
        splitted = re.split(",|;",line[0])
        employee_writer.writerow(splitted)
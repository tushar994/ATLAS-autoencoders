import csv
import re

employee_file = open('only_j.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# employee_writer.writerow(['John Smith', 'Accounting', 'November'])
# employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open("only_particles.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        # print(line[0])
        splitted = re.split(",",line[0])
        # print(splitted)
        if(splitted[0]=='j'):
            employee_writer.writerow(splitted[1:])
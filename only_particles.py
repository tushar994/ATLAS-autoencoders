import csv
import re

employee_file = open('only_particles.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# employee_writer.writerow(['John Smith', 'Accounting', 'November'])
# employee_writer.writerow(['Erica Meyers', 'IT', 'March'])

with open("my_info.csv", "r") as f:
    reader = csv.reader(f, delimiter="\n")
    for i, line in enumerate(reader):
        # print(line[0])
        splitted = re.split(",",line[0])
        # print(splitted)
        splitted = splitted[5:]
        print(splitted)
        length = len(splitted)
        for j in range(0,length):
            if (j%5==0 and j != length-1):
                employee_writer.writerow(splitted[j:j+5])

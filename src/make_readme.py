import csv

header_path="readme.template.md"
readme_path="../README.md"

d1 = {}

with open("export.csv", "r") as infile:
    reader = csv.reader(infile)
    headers = next(reader)
    n = 0
    for row in reader:
        d1[n] = {key: value for key, value in zip(headers, row)}
        n += 1


header_file = open(header_path,'r')
header_data = header_file.read()
readme = open(readme_path,'w')
readme.write(header_data)


table  = "| Type | Auxiliary Type |Short Name| Long Name|\n"
table += "|:----:|:--------------:|:--------:|----------|\n"
for i in sorted(d1.keys()):
    table += "|{}|{}|{}|{}|\n".format(d1[i]['File type'],d1[i]['Auxiliary Type'], d1[i]['Short name'],d1[i]['Long name'] )

readme.write(table)
    # print(i)
    # print(d1[i]['Short name'])
# new_days.write(days)
# print(days)


readme.close()


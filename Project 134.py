import pandas as pd
import matplotlib.pyplot as plt
import csv

df = []

with open('bright_stars.csv','r') as f:
  csvreader = csv.reader(f)
  for i in csvreader:
    if i != []:
      df.append(i)

headers = df[0]
headers[0] = "Index"
star_rows = df[1:]

distance = []
for i in star_rows:
  if float(i[2]) <= 100:
    distance.append(i)
  else:
    pass

gravity = []

for i in distance:
  if float(i[5].split(' ')[0]) > 150 and float(i[5].split(' ')[0]) < 350:
    gravity.append(i)
  else:
    pass

with open('output_stars.csv','w') as f:
  csvWriter = csv.writer(f)
  csvWriter.writerow(headers)
  csvWriter.writerows(gravity)
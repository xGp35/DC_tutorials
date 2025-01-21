import pandas as pd
import csv

temperatures = pd.read_csv('temperatures.csv')

temperatures.to_csv('temp.csv', index = False)


with open('temp.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(','.join(row))
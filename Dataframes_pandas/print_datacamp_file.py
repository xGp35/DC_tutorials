import pandas as pd
avocados = pd.read_csv('avocados.csv')

import csv

avocados.to_csv('avocados.csv', index=False)
with open('avocados.csv','r') as fil:
    csv_reader = csv.reader(fil)
    for row in csv_reader:
        print(','.join(row))




# Function to read and print CSV file
def read_and_print_csv(file_path):
    with open(file_path, mode='r', newline='') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(','.join(row))

# Example usage
file_path = 'example.csv'
read_and_print_csv(file_path)
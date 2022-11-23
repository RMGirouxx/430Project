import csv
import sys
import pandas as pd

original_df = pd.read_csv('languages.csv')
split_df = pd.DataFrame()

with open(original_df, 'r') as csv_in_file:
    with open(split_df, 'w') as csv_out_file:
        reader = csv.reader(csv_in_file, delimiter=';')
        writer = csv.writer(csv_out_file, delimiter=',')
        for row in reader:
            print(row)
            writer.writerow(row)


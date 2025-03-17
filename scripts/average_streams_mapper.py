#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin, delimiter=',')

for row in reader:
    if len(row) < 9:  # Ensure enough columns exist
        continue
    region = row[5]  # Assuming region is in column 5
    streams = row[8]  # Assuming streams count is in column 8

    try:
        streams = float(streams)  # Convert streams to float
        print(f"{region}\t{streams}\t1")
    except ValueError:
        continue

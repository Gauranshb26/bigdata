#!/usr/bin/env python3
import sys
import csv

reader = csv.reader(sys.stdin, delimiter=',')

for row in reader:
    if len(row) < 7:
        continue
    region = row[5]  # Assuming region is in column 5
    genre = row[6]   # Assuming genre is in column 6

    print(f"{region}\t{genre}\t1")

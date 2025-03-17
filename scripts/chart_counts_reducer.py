#!/usr/bin/env python3
import sys

current_key = None
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        key, value = line.rsplit("\t", 1)
        value = int(value)
    except ValueError:
        continue

    if key == current_key:
        count += value
    else:
        if current_key is not None:
            print(f"{current_key}\t{count}")
        current_key = key
        count = value

# Print last key's results
if current_key is not None:
    print(f"{current_key}\t{count}")

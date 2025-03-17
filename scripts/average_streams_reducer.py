#!/usr/bin/env python3
import sys

current_region = None
total_streams = 0
total_count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        region, streams, count = line.split("\t")
        streams = float(streams)
        count = int(count)
    except ValueError:
        continue

    if region == current_region:
        total_streams += streams
        total_count += count
    else:
        if current_region is not None:
            print(f"{current_region}\t{total_streams / total_count}")
        current_region = region
        total_streams = streams
        total_count = count

# Print last region's results
if current_region is not None:
    print(f"{current_region}\t{total_streams / total_count}")

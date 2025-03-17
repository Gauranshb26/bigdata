#!/usr/bin/env python3
import sys
from collections import defaultdict

current_region = None
genre_counts = defaultdict(int)

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        region, genre, count = line.split("\t")
        count = int(count)
    except ValueError:
        continue

    if region == current_region:
        genre_counts[genre] += count
    else:
        if current_region is not None:
            most_common_genre = max(genre_counts, key=genre_counts.get)
            print(f"{current_region}\t{most_common_genre}")
        
        current_region = region
        genre_counts.clear()
        genre_counts[genre] = count

# Print last region's most common genre
if current_region is not None:
    most_common_genre = max(genre_counts, key=genre_counts.get)
    print(f"{current_region}\t{most_common_genre}")

import pandas as pd
import time

youtube_trends = pd.read_csv("youtube_trend_chaser/US_youtube_trending_data.csv")

start = time.time()
tags_number = youtube_trends["tags"].str.split("|").iloc[0:5]

tag_dict = {}

for tag in tags_number:
    for t in tag:
        if t not in tag_dict.keys():
            tag_dict[t] = 1
        else:
            tag_dict[t] = tag_dict[t] + 1

for tag, cnt in tag_dict.items():
    print(tag, cnt)

end = time.time()
print(f"Execution time: {end - start:.6f} seconds")


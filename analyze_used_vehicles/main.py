import pandas as pd

data = pd.read_csv("analyze_used_vehicles/car details v4.csv", index_col = False) # read the csv without addinng an index column
print(data)

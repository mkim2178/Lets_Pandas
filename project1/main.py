import pandas as pd

data = pd.read_csv("project1/car details v4.csv", index_col = False) # read the csv without addinng an index column
print(data)
# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows():
    print(lab + ": " + str(row['cars_per_cap']))

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    print(lab)
    print(row)
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)
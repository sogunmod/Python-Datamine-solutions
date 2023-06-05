x = 6
print(f'x:{x}')
y = 8
print(f'y:{y}')
z = x*y
print(f'z:{z}')


x, y, z = "peanutbutter", "peanutbutter", "peanutbutter"
print(f'x, y, z : {x}, {y}, {z}')

club_sandwich = ["bread", "butter", "egg", "tomatoes"]
print(f'club sandwich is:{club_sandwich}')


import pandas as pd
disney= pd.read_csv("/anvil/projects/tdm/data/disney/flight_of_passage.csv")
disney


print(disney.head())

print(disney.tail())

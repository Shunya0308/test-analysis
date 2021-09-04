import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob

# Consolidate csv files into a single file
csv_files = glob.glob('result/*.csv')

# Show summarized file names
for a in csv_files:
    print(a)

# Store the summarized files in a list
data_list = []

for file in csv_files:
    data = pd.read_csv(file)
    data_list.append(data)

# Store in df
df = pd.concat(data_list, axis=0, sort=True)

# Save a summary file
df.to_csv("total_file.csv", index=False)

# Output total_file
df = pd.read_csv("total_file.csv")

# Extract the file
df_total = df[['中分類','正誤']]

# Change column names
df_total = df_total.rename(columns={'正誤': '正答率'})

# Converting symbols to numbers
df_total = df_total.replace(['○','×'], [100,0])

# Calculate the average
df_total = df_total.groupby('中分類').mean()

# Decimal points are rounded down
pd.options.display.float_format ='{:.0%}'.format

# Sort the percentage of correct answers
df_total = df_total.sort_values('正答率')

# Change the character encoding of matplotlib
plt.rcParams['font.family'] = 'Hiragino sans GB'

# Output bar graph
df_total.plot(kind='barh', rot=0, figsize=(10,12), color=['#4f9982','#8b5f00'], grid=True, fontsize=12)

# View figure
plt.show()
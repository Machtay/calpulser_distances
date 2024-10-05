import pandas as pd
import sqlite3
import numpy as np

# Step 1: Connect to the SQLite database
conn = sqlite3.connect('AntennaInfo.sqlite')

# Step 2: Read the desired columns from your table into a DataFrame
query = "SELECT antLocationX, antLocationY, antLocationZ FROM ARA04"
df = pd.read_sql_query(query, conn)
df = df.head(16)

# Close the database connection
conn.close()

# Step 3: Calculate the average of each column
avg_column1 = df['antLocationX'].mean()
avg_column2 = df['antLocationY'].mean()
avg_column3 = df['antLocationZ'].mean()

# Step 4: Use the average values to compute the coordinate
average_coordinate = np.sqrt(avg_column1**2 + avg_column2**2 + avg_column3**2)

print("The average coordinate is:", average_coordinate)
print("Average coordinate positions: ", avg_column1, ",", avg_column2, ",", avg_column3)
print(df.tail())

import sqlite3
import pandas as pd

# Connect to the SQLite database
conn = sqlite3.connect('wine_data.db')

"""
Select "alcohol", "flavanoids", "total_phenols", "target" of the wines with an alcohol content greater than the average alcohol content.
Save the result in a csv file.
"""

query = """
SELECT alcohol, flavanoids, total_phenols, target
FROM wine_data
WHERE alcohol > (SELECT AVG(alcohol) FROM wine_data);
"""

# Execute a SELECT query and read the results into a DataFrame
df = pd.read_sql_query(query, conn)

# Close the connection
conn.close()

# Print the DataFrame
print(df)

# Save the df as "feat"
df.to_csv("wine_features.csv", index=False)
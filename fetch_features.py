import sqlite3
import pandas as pd

"""
Select "alcohol", "flavanoids", "total_phenols", "target" of the wines with an alcohol content greater than the average alcohol content.
Save the result in a csv file.
"""

## YOUR CODE HERE
query = """

"""

# Connect to the SQLite database
conn = sqlite3.connect('wine_data.db')

# Execute a SELECT query and read the results into a DataFrame
## YOUR CODE HERE
## Read the doc and find the args
df = pd.read_sql_query()

# Close the connection
conn.close()

# Print the DataFrame
print(df)

# Save the df
## YOUR CODE HERE
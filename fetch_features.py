import sqlite3
import pandas as pd

"""
Select "alcohol", "flavanoids", "total_phenols", 
"target" of the wines with an alcohol content greater than the average alcohol content.
Save the result in a csv file.
"""

## YOUR CODE HERE
query = """
    SELECT alcohol, flavanoids, total_phenols, target
    FROM wine_data
    WHERE alcohol > (SELECT AVG(alcohol) FROM wine_data);
"""

# Connect to the SQLite database
conn = sqlite3.connect("wine_data.db")

# Execute a SELECT query and read the results into a DataFrame
## YOUR CODE HERE
## Read the doc and find the args
df = pd.read_sql_query(query, con=conn)

# Close the connection
conn.close()

# Print the DataFrame
print(df)

# Save the df
## YOUR CODE HERE
df.to_csv("alcohol_content_greater_than_average.csv")

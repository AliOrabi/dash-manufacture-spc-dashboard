# Step 1: Import the necessary libraries
import pandas as pd

# Step 2: Create a List of Dictionary items
signal =[{'pattern': {'signal': 'Bear', 'date': '2020-01-11'}, 'code': 532648, 'company_name': 'YESBANK'},
{'pattern': {'signal': 'Bull', 'date': '2020-01-11'}, 'code': 532839, 'company_name': 'DISHTV'}, 
{'pattern': {'signal': 'Bear', 'date': '2020-01-11'}, 'code': 533122, 'company_name': 'RTNPOWER'},
{'pattern': {'signal': 'Bull', 'date': '2020-01-11'}, 'code': 539310, 'company_name': 'TISL'}, 
{'pattern': {'signal': 'Bull', 'date': '2020-01-11'}, 'code': 514183, 'company_name': 'BLACKROSE'} ]

# Step 3: Create a Dataframe

df = pd.DataFrame(signal)
df.to_csv('text.csv', mode='a')

# Step 4: Create a Dataframe

rows = []

df1 = df["pattern"] # df is the dataframe for the above signal
for row,code,name in zip(df1,df["code"],df["company_name"]):
    row["code"] = code
    row["name"] = name
    rows.append(row)
rows
df2 = pd.DataFrame(rows).to_csv('text.csv', mode='a')
df2
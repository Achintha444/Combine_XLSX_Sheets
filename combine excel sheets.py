import pandas as pd

# Load the first XLSX sheet with columns [Key, Value]
df1 = pd.read_excel("english.xlsx")

# Load the second XLSX sheet with columns [Key, Chinese]
df2 = pd.read_excel("chinese.xlsx")

# Merge the dataframes based on the 'Key' column using an outer join
merged_df = df1.merge(df2, on='Key', how='outer')

# Reorder the columns to [Key, Value, Chinese]
merged_df = merged_df[['Key', 'Value', 'Chinese']]

# Add an empty row above rows starting with '#'
for index, row in merged_df.iterrows():
    if str(row['Key']).startswith('#'):
        merged_df = pd.concat([merged_df.iloc[:index], pd.DataFrame([['', '', '']], columns=merged_df.columns), merged_df.iloc[index:]])

# Remove duplicate rows based on the 'Key' column
merged_df = merged_df.drop_duplicates(subset=['Key'])

# Save the merged dataframe to a new XLSX file
merged_df.to_excel("combined_sheet.xlsx", index=False, engine='openpyxl')

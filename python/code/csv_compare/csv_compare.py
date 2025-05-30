import pandas as pd
print("hello")

file1 = 'file1.csv'
file2 = 'file2.csv'

file3 = 'file3.xlsx'
file4 = 'file4.xlsx'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

# df1 = pd.read_excel(file3)
# df2 = pd.read_excel(file4)

# Compare the DataFrames
# Find rows that are different
diff_rows = pd.concat([df1, df2]).drop_duplicates(keep=False)

# Find columns that are different
# This will give you a DataFrame with only the differing columns
diff_columns = df1.compare(df2)

# Display the results
print("Different Rows:")
print(diff_rows)

print("\nDifferent Columns:")
print(diff_columns)
import pandas as pd

# Create a DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)

# Multiply columns 'A' and 'B', and store the result in a new column 'Result'
df['Result'] = df['A'].multiply(df['B'])

# Display the updated DataFrame
print(df)

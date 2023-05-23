import pandas as pd

# Load spreadsheet
xl = pd.read_excel('data_type.xlsx')

# Print the data type of each column
print(xl.dtypes)

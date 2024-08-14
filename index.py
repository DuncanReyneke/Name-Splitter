import pandas as pd

# Replace 'your_input_file.xlsx' with the path to your input Excel file
input_file = 'OneYearNoteMaturities_08-24.xls'
output_file = 'Revised_OneYearNoteMaturities_08-24.xlsx'

# Read data from the Excel file
df = pd.read_excel(input_file)

# Function to split names
def split_name(name):
    # Convert name to lowercase for comparison
    lower_name = name.lower()
    # Check if the name contains keywords indicating a church
    if 'church' in lower_name or 'temple' in lower_name or 'synagogue' in lower_name or 'mosque' in lower_name:
        return pd.Series([name, ''])
    else:
        parts = name.split()
        # If there are exactly 2 parts, it's a first and last name
        if len(parts) == 2:
            return pd.Series(parts)
        # If there are more than 2 parts, consider the first part as the first name and the last part as the last name
        elif len(parts) > 2:
            return pd.Series([parts[0], parts[-1]])
        else:
            return pd.Series([name, ''])

# Apply the function to the DataFrame
df[['First Name', 'Last Name']] = df['Primary Name'].apply(split_name)

# Drop the original 'Entity_Name' column
df.drop(columns=['Primary Name'], inplace=True)

# Write the processed data back to a new Excel file
df.to_excel(output_file, index=False)
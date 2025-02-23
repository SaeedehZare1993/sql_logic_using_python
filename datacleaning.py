import pandas as pd

# Loading data frames
users_df = pd.read_excel('userss.xlsx')
customers_df = pd.read_excel('customers.xlsx')

# Ensure column names are trimmed
users_df.columns = users_df.columns.str.strip()
customers_df.columns = customers_df.columns.str.strip()

# Convert national codes to have one or two zeros at the beginning
def prepend_zeros(NationalCode):
    NationalCode = str(NationalCode).strip().split('.')[0]  # Ensure no leading/trailing spaces
    if len(NationalCode) == 9:
        return '0' + NationalCode
    elif len(NationalCode) == 8:
        return '00' + NationalCode
    return NationalCode

# Change phone number type into string and ensure no formatting issues
users_df['PhoneNumber'] = users_df['PhoneNumber'].astype(str).apply(lambda x: '0' + x.split('.')[0])
customers_df['PhoneNumber'] = customers_df['PhoneNumber'].astype(str).str.zfill(11)


# Apply the function to the NationalCode column
users_df['NationalCode'] = users_df['NationalCode'].apply(prepend_zeros)
customers_df['NationalCode'] = customers_df['NationalCode'].apply(prepend_zeros)

# Convert national codes into string
users_df['NationalCode'] = users_df['NationalCode'].astype(str).str.zfill(10)
customers_df['NationalCode'] = customers_df['NationalCode'].astype(str).str.zfill(10)

# Save the updated DataFrames to new Excel files
users_df.to_excel('updated_users.xlsx', index=False)
customers_df.to_excel('updated_customers.xlsx', index=False)

# Display the updated DataFrames
print(users_df.head())
print(customers_df.head())

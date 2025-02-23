import pandas as pd
def find_conflicts(user_file = 'updated_users (copy).xlsx', customer_file = 'updated_customers (copy).xlsx', output_file='conflict_df.xlsx'):
    df1= pd.read_excel(user_file)
    df2 = pd.read_excel(customer_file)

    merged_file = df1.merge(df2, on='PhoneNumber', how='inner')

    mask = (
      ( merged_file['CustomerName1'] != merged_file['CustomerName'])
      (merged_file['NationalCode1'] != merged_file['NationalCode'])
    )
    conflict_df = merged_file.loc[mask]

    if conflict_df.empty:
        print("No conflict found")
    else:
        print('Cnflict found')
        print(conflict_df)

    conflict_df.to_excel(output_file, index= False)
    return conflict_df

if __name__ == "__main__":
    find_conflicts = find_conflicts()

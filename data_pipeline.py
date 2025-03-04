import pandas as pd

# Load the dataset
file_path = "data.csv"  # Update the path if needed, in this case it's all in the samedirectory
df = pd.read_csv(file_path)

# ==============================
# VALIDATION - MISSING VALUES
# ==============================
# Check for missing values
missing_values = df.isnull().sum() #Add up the total of missing values

# Display columns with missing values
print("Missing values per column:")
print(missing_values)
#replace with this line to only display column with missing values
#print(missing_values[missing_values > 0]) 

# Ask the user if they want to remove the columns with missing values
remove_columns = input("\nDo you want to remove columns with missing values? (yes/no): ")

if remove_columns == 'yes':
    # Remove columns with missing values
    df_cleaned = df.dropna(axis=1) # "na" drops any columns with at least one (axis=1) missing value
    print("\nColumns with missing values have been removed.")
    print("Remaining columns:")
    print(df_cleaned.columns) # Displays the remaining columns

    # Save the cleaned data back to a CSV file
    df_cleaned.to_csv("data_cleaned.csv", index=False)  # Saves to a new file 
    print("\nThe cleaned data has been saved to 'data_cleaned.csv'.")
else:
    print("\nThe columns with missing values have been left alone.")





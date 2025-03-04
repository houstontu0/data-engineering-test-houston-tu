import pandas as pd

# Load the dataset
file_path = "data.csv"  # Update the path if needed, in this case it's all in the samedirectory
df = pd.read_csv(file_path)

# ==========
# VALIDATION
# ==========
# Check for missing values
missing_values = df.isnull().sum() #Add up the total of missing values

# Display columns with missing values
print("Missing values per column:")
print(missing_values)
#replace with this line to only display column with missing values
#print(missing_values[missing_values > 0]) 







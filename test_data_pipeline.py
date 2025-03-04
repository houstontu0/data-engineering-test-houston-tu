import pandas as pd
import numpy as np

# Check for missing values in a data
def test_missing_values():
    # Create  sample data with missing values
    data = {
        'id': [1, 2, 3],
        'diagnosis': ['M', 'B', np.nan],  # 'M' for malignant, 'B' for benign
        'radius_mean': [14.2, np.nan, 13.1]
    }
    df = pd.DataFrame(data)
    
    # Calculate missing values
    missing_values = df.isnull().sum()
    
    # Check that the missing values are correctly identified
    assert missing_values['id'] == 0
    assert missing_values['diagnosis'] == 1
    assert missing_values['radius_mean'] == 1
    

# Check if the columns get removed
    
# Check if new data saves
# data-engineering-test-houston-tu

# Objective
- Read data from a public dataset using Python
- Implement Data Valdiation (e.g., check for missing values, format inconsistencies, etc).
- Transform the data (e.g., removing columns, convert dates to a standard format, etc.)
- Load the data in a new format-structured file (CSV).
- Create unit tests for critical functions
- Document design decisions in the README. 


# Design Decisions
Found a dataset from kaggle.com (simple google search) <br>
Visually scanned the data for any inconsistencies <br>
Data seemed alright, decided to remove a column to create a pipeline for missing values <br>
Columns with missing values will simply be removed instead of replaced <br>
The user was given the choice to remove or leave the column <br>




# Requirements 
To run the data pipeline, ensure you have the following installed:
- Python 3.11.7
- pandas
- pytest

You can install the dependcies using:
`pip3 install -r requirements.txt` 

# How to run 
1. Navigate to the directory of the pipeline. If you're using vsCode, simply open a terminal
2. run `python data_pipeline.py`
3. To run tests, run `python test_data_pipeline.py`
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler 
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder, StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

data_cross = pd.read_csv('D:/Alzheimer/oasis/oasis_cross-sectional.csv')
data_long = pd.read_csv('D:/Alzheimer/oasis/oasis_longitudinal_binary.csv')

import pandas as pd
import numpy as np

# Assuming you have already loaded your data:
# data_cross = pd.read_csv('D:/Alzheimer/oasis/oasis_cross-sectional.csv')

# --- Add the 'Group' column ---

data_cross['Group'] = np.where(
    # Condition: If CDR score is greater than or equal to 0.5
    data_cross['CDR'] >= 0.5,
    
    # Value if True (Demented)
    'Demented',
    
    # Value if False (Nondemented, covering CDR = 0)
    'Nondemented'
)

# --- Verification (Optional) ---

print("Data rows after adding the 'Group' column:")
print(data_cross[['CDR', 'Group']].head())



data_long = data_long.rename(columns={'EDUC':'Educ'})

data = pd.concat([data_cross, data_long])
data.shape
print(data.isnull().sum())

for column in data.columns:
    mode_value = data[column].mode()[0]  
    data[column].fillna(mode_value, inplace=True)

missing_values_after_filling = data.isnull().sum()
print(missing_values_after_filling)


# data.to_csv('D:/Alzheimer/oasis/clean_oasis_data.csv', index=False)
# data.to_excel('D:/Alzheimer/oasis/clean_oasis_data_0.xlsx', index=False)

X = data.drop(['ID', 'Delay', 'Subject ID', 'MRI ID', 'Visit', 'MR Delay'], axis=1)
X.to_excel('D:/Alzheimer/oasis/clean_oasis_data_Clean.xlsx', index=False)
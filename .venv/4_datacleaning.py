import pandas as pd
import numpy as np
# Random data_set
std_info = {
    'ID':[1,2,3,2,1,4,5,6],
    'Name':["Ali",None,"Ahmet","Mehmet",None,"Zeynep","Ayşe","Fatma"],
    'Age':[25,30,np.nan,35,40,28,22,"Empty"],

}
df = pd.DataFrame(std_info)
print("Before Cleaning:")
print(df)
print("\nAfter Cleaning:")
# Drop rows with missing values
df_cleaned = df.drop_duplicates(subset=['ID'],keep='first',inplace=False)
df_cleaned['Name']= df_cleaned['Name'].fillna("Haider")
df_cleaned["Age"]=pd.to_numeric(df_cleaned["Age"],errors ='coerce')
df_cleaned['Age']= df_cleaned['Age'].fillna(df_cleaned['Age'].mean())
df_cleaned['Age']= df_cleaned['Age'].astype(int)
print(df_cleaned)

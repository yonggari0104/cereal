import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


cer = pd.read_csv('C:\\Users\\user\\.spyder-py3\\cereal\\cereal.csv')


#SEE IF NaN VALUES EXISTS
print(cer.isna().any())

print(cer.info())
print(cer.head())
print(cer.dtypes)
print(cer.describe())

#%%

print(cer['mfr'].value_counts())

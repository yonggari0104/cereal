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







#MANUFACTURER BREAKDOWN
print(cer.groupby('mfr').describe())

#PRINTS EACH MANUFACTURER'S CEREAL NUMBER COUNT
print(cer['mfr'].value_counts())

#MANUFACTURER GROUP 'P' CONTAINS THESE CEREALS
print(cer['name'][cer['mfr'] == 'P'])

#PIE GRAPH OF MANUFACTURER
labels = 'Kelloggs', 'American Home Food Product','General Mills','Post', 'Quaker Oats', 'Ralston Purina', 'Nabisco'
sizes = [23,1,22,9,8,8,6]
explode = (0.1,0.1,0,0,0,0,0)
plt.pie(sizes, labels=labels,shadow = True, startangle=90, explode = explode, autopct='%1.1f%%')
plt.show()


#BAR GRAPH OF COUNT FOR MANUFACTURERS AND CEREAL TYPE
fig, axes = plt.subplots(1,2,figsize=(10, 5))
sns.countplot(x="mfr", data=cer, ax=axes[0], palette="Set2")
sns.countplot(x="type", data=cer, ax=axes[1], palette="Set3")






#SODIUM BREAKDOWN
#COUNT FOR SODIUM FOR HOT CEREALS
hot_cer=cer["sodium"][cer["type"] == "H"]
print(hot_cer.mean())
#COUNT FOR SODIUM FOR COLD CEREALS
cold_cer = cer["sodium"][cer["type"] == "C"]
print(cold_cer.mean())








#RATING BREAKDOWN
#SIDE BAR CHART OF CEREAL RATINGS
cer_rate = cer.sort_values(['rating'],ascending=False).reset_index(drop=True)
plt.figure(figsize=(20,20))
sns.barplot(x=cer_rate["rating"],y=cer_rate["name"])
plt.xlabel("Product Name",fontsize=15)
plt.ylabel("Rating",fontsize=15)
plt.title("Product Rating",fontsize=15)
plt.show()








#SHELF BREAKDOWN
print(cer['name'][cer['shelf'] == 1].count()) 
print(cer['name'][cer['shelf'] == 2].count()) 
print(cer['name'][cer['shelf'] == 3].count()) 


























import pandas as pd
import matplotlib.pyplot as plt

#Crosstab
#Agregar el csv al dataframe 
df = pd.read_csv ('mineriadatos/users-modify.csv')
#Seleccionar columnas para analisis
df = df[['is_admin','company']]
#print(df.head(6))

pd.crosstab(df['is_admin'],df['company']).plot(kind='bar')
plt.show()
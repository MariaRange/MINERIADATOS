# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

#agroup by
#Agregar el csv al dataframe
df = pd.read_csv('mineriadatos/users-modify.csv')

#Seleccionar columnas para analisis
df = df[['gender','company']]
#print(df.head(6))

#Agrupar gender y role del dataframe
group=df.groupby(['gender','company'])
print(group.size().reset_index(name='counts'))
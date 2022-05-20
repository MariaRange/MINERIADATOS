# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

#agroup by
#Agregar el csv al dataframe
df = pd.read_csv('mineriadatos/users-modify.csv')

#PRIMER COLUMNA------------------------------------------------------------------------------------------------------------------------------------
#Seleccionar columnas para analisis
df1 = df[['first_name','car']]
#print(df.head(6))

#Agrupar gender y role del dataframe
group=df1.groupby(['first_name','car'])
print(group.size().reset_index(name='counts'))


#SEGUNDA COLUMNA-----------------------------------------------------------------------------------------------------------------------------------
#Seleccionar columnas para analisis
df2 = df[['last_name','email']]
#print(df.head(6))

#Agrupar gender y role del dataframe
group=df2.groupby(['last_name','email'])
print(group.size().reset_index(name='counts'))


#TERCER COLUMNA------------------------------------------------------------------------------------------------------------------------------------
#Seleccionar columnas para analisis
df3 = df[['favorite_app','avatar']]
#print(df.head(6))

#Agrupar gender y role del dataframe
group=df3.groupby(['favorite_app','avatar'])
print(group.size().reset_index(name='counts'))


#CUARTA COLUMNA-----------------------------------------------------------------------------------------------------------------------------------
#Seleccionar columnas para analisis
df4 = df[['active','department']]
#print(df.head(6))

#Agrupar gender y role del dataframe
group=df4.groupby(['active','department'])
print(group.size().reset_index(name='counts'))
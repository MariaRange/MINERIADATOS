import pandas as pd
import matplotlib.pyplot as plt

#Agregar el archivo para analisis con pandas
df = pd.read_csv ('mineriadatos/titanic.csv')

#Consultar de ,manera rapida si esta conectando con el dataset
#print(df.head(6))
#Conocer la dimension del dataset 
#print(df.shape)

#Conocer si hay datos duplicados
#print(df.duplicated().sum())

#Conocer info de dataset
#print(df.info)

#Conocer la descripcion del database
#print(df.describe())

#Contar el numero de registros por columna
#print(df.count())

#Cambiar datos null por un 2 para desconocido
df['Survived'] = df['Survived'].fillna(2)

#Cambiar datos null por S/C en columna cabin
df['Cabin'] = df['Cabin'].fillna('S/C')
print(df.count())

#Cambiar un diccionario con los valores originales por valores
# de reemplazo
d = {'male' : 'M', 'female': 'F' }

#Utilizamos un lambda para el reemplazo en una sola linea
df['Sex'] = df['Sex'].apply(lambda x:d[x])
#for x in df['Sex']:
#    df['Sex'] = df['Sex'].apply(d[x])

#Conocer el dataset con valores cambiados
#print(df['Sex'])

#Obtener los nombres de las columnas en una lista
col_names = df.columns.tolist()

#Iterar sobre la lista
#for column in col_names:
    #print("Valores nulos en <" + column + ">": + str(df[column].isnull))

#Cruce de tabla de informacion
ct = pd.crosstab(df['Survived'],df['Sex']).plot(kind='bar')
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad de sobrevivientes por genero")

for barra in ct.containers:
    ct.bar_label(barra, label_type='edge')

plt.show()
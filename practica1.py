# Importar pandas 
import pandas as pd

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/users_data2.csv')

# Imprimir 5 registros
#print(df.head())

# Dimencion del dataset/ dataframe
#print(df.shape)

# Nombre de tipo o dictado de columna
#print(df.dtypes)

# Consideraciones de rendimiento (columnas,datos nulos, dtypes, peso, etc)
#print(df.info())

# Describir dataframe
# Muestra el numero de datos de cada columna, datos unicos, es que mas se repite, asi como la frecuencia 
#print(df.describe())

#Conocer la cantidad de datos faltantes por cada columna
#Muestra la cantidad de filas faltantes 
#print(df.count())

#Conocer si hay datos duplicados
#print(df.duplicated().sum())

#Obtener los nombres de las columnas en una lista
col_names = df.columns.tolist()
#Iterar sobre la lista
for column in col_names:
    #Conocer valores nulos
    print("Valores nulos en <" + column + ">: " + str(df[column].isnull().sum()))
    #Conocer tipo de dato por columna
    print("Tipo de valor de <" + column + ">: " + str(df[column].dtypes))

#Llenar la columna avatar con una url por default
df['avatar'] = df['avatar'].fillna('default.png')
df['lenguage'] = df['lenguage'].fillna('Desconocido')
df['gender'] = df['gender'].fillna('D')

df.to_csv('mineriadatos/users-modify.csv' , index=False)
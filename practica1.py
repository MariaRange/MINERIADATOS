# Importar pandas 
import pandas as pd
import matplotlib.pyplot as plt

# Empezar a leer el archivo csv
df = pd.read_csv('mineriadatos/train.csv')

#Consultar de ,manera rapida si esta conectando con el dataset
print("----------------CONEXION--------------------")
print(df.head(6))

#Conocer la dimension del dataset 
print("---------------DIMENSION--------------------")
print(df.shape)

#Conocer info de dataset
print("---------------INFORMACION------------------")
print(df.info)

#Contar el numero de registros por columna
print("----------REGISTROS POR COLUMNA-------------")
print(df.count())

#Conocer si hay datos duplicados
print("------------DATOS DUPLICADOS----------------")
print(df.duplicated().sum())

# Llenar los campos nulos
col_names =df.columns.tolist()
print("--------------VALORES NULOS-----------------")
for column in col_names :
    print( "Valores nulos en  <"+ column + ">: "  + str (df[column].isnull().sum()))

# Llenar valores nulos en las columnas
df['Age'] = df['Age'].fillna(0)  
df['Cabin'] = df['Cabin'].fillna("Unknown") 
df['Embarked'] = df['Embarked'].fillna("U")    

print("--------------COMPROBACION------------------")
df.to_csv('mineriadatos/train_completo.csv', index=False)
df_completo = pd.read_csv('mineriadatos/train_completo.csv')
print(df_completo.count())

# Crear 3 crosstab para conocer mas del dataset con tablas.
#Grafica  Numero 1
df_completo3 = df_completo[['Survived', 'Pclass']]
ct3 = pd.crosstab(df_completo3['Survived'],df_completo3['Pclass']).plot(kind='bar')
plt.legend(title = "Pclass") 
plt.title("Grafica 1. Sobrevivio y Pclass")
plt.xlabel("Sobrevivio")
plt.xticks([0, 1], ['No', 'Si'])
plt.show()

#Grafica Numero 2
df_completo1 = df_completo[['Age', 'Sex']]
ct = pd.crosstab(df['Age'],df['Sex']).plot(kind='bar')
plt.legend(title = "Sexo") 
plt.title("Grafica 2. Edad y Sexo")
plt.xlabel("Edad")
plt.yticks([0, 1], ['Femenino', 'Masculino'])
plt.show()

#Grafica Numero 3
df_completo2 = df_completo[['Survived', 'Sex']]
ct2 = pd.crosstab(df_completo2['Survived'],df_completo2['Sex']).plot(kind='bar')
plt.legend(title = "Genero") 
plt.title("Grafica 3. Sobrevivientes y Sexo")
plt.xlabel("Sobrevivio")
plt.xticks([0, 1], ['No', 'Si'])
plt.show()
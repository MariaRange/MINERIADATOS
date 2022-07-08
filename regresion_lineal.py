import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv("mineriadatos/insurance.csv")
print('Los datos del dataframe son = ')
print(df)

print(df.shape)
print(df.info)
print(df.describe)

d = {'female' : 1, 'male' : 0} 
#Utilizados en lambda para el reemplazo de una sola linea
df['sex'] = df['sex'].apply(lambda x:d[x])
print(df)

d = {'yes' : 1, 'no' : 0}
#Utilizados en lambda para el reemplazo de una sola linea
df['smoker'] = df['smoker'].apply(lambda x:d[x])
print(df)

d = {'southwest' : 1, 'northwest' : 2, 'southeast' : 3, 'northeast' : 4 }
#Utilizados en lambda para el reemplazo de una sola linea
df['region'] = df['region'].apply(lambda x:d[x])

#Seleccionar las columnas a procesar 
df1 = df[['region', 'sex', 'charges']]

#Crear un cruce entre columnas y filas
ct = pd.crosstab([df['sex']], df1['region']).plot(kind='bar')
plt.title('Grafica para cruce de region y genero')
plt.xlabel("Region")
plt.ylabel("Genero")
plt.show()


all_cols = df.to_numpy()
#Label data is stored into y (predictors)
y = all_cols[:,6]
y = np.array(y)
print('y =', y)

#Pixel information is stored into x (predictors)
x = all_cols[:,0:6]
x = np.array(x)
print('x =')
print(x)

plt.scatter(x[:,0], y)
plt.show()

#Creamos modelo (inicializamos nuestra regresion lineal)
model = LinearRegression()
model.fit(x, y)

#Analizar el modelo entrenando
r_sq = model.score(x, y)
print()
print()

print('coefficient of determination', r_sq)

print()
print()
print('-------------------------Resultados del modelo matematico de regresion--------------------------')
print()
print()
print('intercept (b):', model.intercept_)
print('slope (s):', model.coef_)


# Age sex BMI Children smoker region
#x_pred = [21, 1, 30.60, 1, 2, ]

print('Insertar los valores de las variables independientes -x- medidas para predecir')
print('la variable independiente -charges-')
x_pred = np.array([20.0, 1.0, 20.60, 0.0, 0.0, 4.0]).reshape((-1, 1))
print(x_pred.T)

y_pred = model.predict(x_pred.T)
print('predicyted response:', y_pred, sep='\n')

#Save model 
open('medicalcost.pkl', 'wb')
pickle.dump(model, open('medicalcost.pkl', 'wb'))
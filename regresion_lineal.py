import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_csv('mineriadatos/insurance.csv')
print('los datos del dataframe son = ')

d = {'female': 1, 'male': 0}
# utilizando lambda para el reemplazo en una sola linea
df['sex'] = df['sex'].apply(lambda x: d[x])

d = {'yes': 1, 'no': 0}
# utilizando lambda para el reemplazo en una sola linea
df['smoker'] = df['smoker'].apply(lambda x: d[x])

d = {'southwest': 1, 'northwest': 2, 'southeast': 3, 'northeast': 4}
# utilizando lambda para el reemplazo en una sola linea
df['region'] = df['region'].apply(lambda x: d[x])

#df1 = df[['region','sex','charges']]
#ct = pd.crosstab([df1['sex']], df1['region']).plot(kind='bar')
#plt.title('grafica para cruce de region y genero')
# plt.xlabel('Genero')
# plt.ylabel('# personas')
# plt.show()

all_cols = df.to_numpy()
# label data is stored into (prediction)
y = all_cols[:, 6]
y = np.array(y)
print('y = ', y)

x = all_cols[:, 0:6]
x = np.array(x)
print('x = ')
print(x)

plt.scatter(x[:, 0], y)
# plt.show()

# NO ENTENDI
model = LinearRegression()
model.fit(x, y)

# ANALIZAR EL MODELO ENTRENADO
r_sq = model.score(x, y)
print()
print()
print('Coefficient of determination: ', r_sq)
print()
print()
print('---------regresion del modelo matematico de regresión-----------')
print()
print()
print('intercept (b): ', model.intercept_)
print('slope(s): ', model.coef_)
print()

print()
print()
print('Insertar los valores de las variables independietes -x- medidas para predecir')
print('la variable de independietne -charges-')
print()
print()
x_pred = np.array([20.0, 1.0, 20.60, 0.0, 0.0, 4.0]).reshape((-1, 1))
print(x_pred.T)
print()

y_pred = model.predict(x_pred.T)
print('predicated response: ', y_pred, sep='\n')

# save the model
open('medicalcost.pkl', 'wb')
pickle.dump(model, open('medicalcost.pkl', 'wb'))

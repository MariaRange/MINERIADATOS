import pandas as pd
import matplotlib.pyplot as plt

#Crosstab
#Agregar el csv al dataframe 
df = pd.read_csv ('mineriadatos/users-modify.csv')
#Seleccionar columnas para analisis
df = df[['gender','car']]
#print(df.head(6))

ct = pd.crosstab(df['gender'],df['car']).plot(kind='bar')
plt.title('Grafica de generos y autos')
#plt.scatter(x=[1], y=[6])
plt.ylabel("Companias")
plt.xlabel("Administrador")
plt.legend(loc='lower left')

#print(ct.containers)
for barra in ct.containers:
    print(barra)
    ct.bar_label(barra, label_type='edge')

plt.savefig('grafica_gender.png')
plt.show()
from sklearn.datasets import fetch_california_housing
import pandas as pd
california =  fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df.head()
df.describe()

# Criar classes para a variável HouseAge
classes = pd.cut(df['HouseAge'], bins=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# Contar a frequência de valores em cada classe 
freq_por_classe = classes.value_counts()

# Exibir a distribuição de frequência por classe da HouseAge
print("\n Distribuição de frequência por classe da HouseAge:")
print(freq_por_classe)
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import pickle
import os

# Carrega os dados
df = pd.read_csv('casas.csv')

# Divide os dados em variáveis independentes (X) e dependentes (y)
X = df.drop('preco', axis=1)
y = df['preco']

# Divide os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
  X, y, test_size=0.2, random_state=42)

# Cria o modelo de regressão linear
modelo = LinearRegression()

# Treina o modelo
modelo.fit(X_train, y_train)

# Faz previsões no conjunto de teste
y_pred = modelo.predict(X_test)

# Avalia o modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
print(f'R^2 Score: {r2:.2f}')
print(f'Mean Absolute Error: {mae:.2f}')

# Salva o modelo treinado em um arquivo
modelo_path = os.path.join(os.path.dirname(__file__), '../app/modelo.pkl')
pickle.dump(modelo, open(modelo_path, 'wb'))
